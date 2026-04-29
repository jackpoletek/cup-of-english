import logging
import time

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import OperationalError, transaction, IntegrityError

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.conf import settings
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

from .utils import generate_activation_link

from .forms import ProfileForm
from enrollments.models import Enrollment
from .models import UserProfile

logger = logging.getLogger(__name__)


# Activation email helper
def send_activation_email(user, request):
    activation_link = generate_activation_link(request, user)

    html_content = render_to_string(
        "emails/activation_email.html",
        {
            "user": user,
            "activation_link": activation_link,
        }
    )

    text_content = strip_tags(html_content)

    email_message = EmailMultiAlternatives(
        subject="Activate your account",
        body=text_content,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email],
    )

    email_message.attach_alternative(html_content, "text/html")

    # Prevent crash leaking to user if email fails to send, but log the issue for debugging
    try:
        email_message.send(fail_silently=False)  # Log email sending issues
    except Exception:
        logger.exception("Error sending activation email.")
        raise


# Role helpers
def user_is_teacher(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "teacher"


def user_is_learner(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "learner"


# Login
def login_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:profile")

    # Support next parameter for redirecting after login
    next_url = request.GET.get("next") or request.POST.get("next")  # Support GET and POST for next parameter

    if next_url in ["", None, None]:
        next_url = None  # Prevent empty string from being treated as a valid URL

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        if not username or not password:
            messages.error(request, "Both fields are required.")
            return render(
                request,
                "accounts/login.html",
                {
                    "next": next_url,  # Preserve next parameter in case of error
                }
            )

        user = authenticate(request, username=username, password=password)

        # Block login if email not verified
        if user is not None:
            if not user.is_active:
                messages.error(request, "Please verify your email address first.")
                return render(
                    request,
                    "accounts/login.html",
                    {
                        "next": next_url,
                    }
                )

            auth_login(request, user)

            # Redirect to next URL if provided, otherwise go to profile
            if next_url:
                return redirect(next_url)

            return redirect("accounts:profile")
        else:
            messages.error(request, "Invalid username or password.")

    return render(
        request,
        "accounts/login.html",
        {
            "next": next_url,
        }
    )


# Resend activation helper
def resend_activation(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip()

        if not email:
            messages.error(request, "Email is required.")
            return redirect("accounts:login")

        try:
            user = User.objects.get(email=email)

            if user.is_active:
                messages.info(request, "Account already activated. You can now log in.")
                return redirect("accounts:login")

            last_sent = request.session.get("last_activation_email_sent", 0)
            now = time.time()

            if now - last_sent < 60:  # 1 minute cooldown
                messages.error(request, "Activation email was sent. Please wait before requesting again.")
                return redirect("accounts:login")

            send_activation_email(user, request)

            request.session["last_activation_email_sent"] = now

            messages.success(request, "Activation email resent.")

        except User.DoesNotExist:
            messages.error(request, "No account found with this email.")

        except Exception:
            # Log the error but avoid leaking information to the user
            messages.error(request, "Resending activation email failed. Please try again later.")
            logger.exception("Error resending activation email.")

    return redirect("accounts:login")


# Logout
def logout_view(request):
    if request.user.is_authenticated:
        auth_logout(request)

    return render(request, "accounts/logout.html")


# Registration
def register_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:profile")

    if request.method == "GET":
        return render(request, "accounts/register.html")

    try:
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()
        password_again = request.POST.get("password_again", "").strip()
        role = request.POST.get("role", "").strip()

        # Validation
        if not all([username, email, password, password_again, role]):
            messages.error(request, "All fields are required.")
            return render(request, "accounts/register.html")

        if role not in ["teacher", "learner"]:
            messages.error(request, "Please select a valid role.")
            return render(request, "accounts/register.html")

        if password != password_again:
            messages.error(request, "Passwords do not match.")
            return render(request, "accounts/register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, "accounts/register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return render(request, "accounts/register.html")

        # Use atomic transaction to ensure both User and UserProfile are created together
        with transaction.atomic():
            # User created with inactive status until email verification
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                is_active=False
            )

            # Profile is automatically created by signals, just setting the role
            user.userprofile.role = role
            user.userprofile.save()

        # User rollback will occur if email sending fails
        send_activation_email(user, request)

        messages.success(
            request,
            "Account created successfully. Check your email for activation instructions."
        )
        return redirect("accounts:login")

    except IntegrityError:
        logger.exception("Error during registration.")
        messages.error(request, "Registration failed. Please try again later.")
        return render(request, "accounts/register.html")
    
    except OperationalError:
        logger.exception("Database error during registration.")
        messages.error(request, "System is temporarily unavailable. Please try again later.")
        return render(request, "accounts/register.html", status=503)
    
    except Exception:
        # Handle unexpected errors gracefully without exposing details to the user, but log them for debugging
        logger.exception("Registration failed.")
        messages.error(request, "Registration failed. Please try again later.")
        return render(request, "accounts/register.html")


# Account Activation
def activate_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return render(request, "accounts/activation_success.html")
        else:
            return render(request, "accounts/activation_failed.html")

    except Exception:
        return render(request, "accounts/activation_failed.html")


# Authenticated views
@login_required
def profile(request):

    # Role-based enrollments
    if hasattr(request.user, "userprofile"):

        if request.user.userprofile.role == "learner":
            enrollments = Enrollment.objects.filter(
                learner=request.user,
                is_active=True
            )

        elif request.user.userprofile.role == "teacher":
            enrollments = Enrollment.objects.filter(
                teacher=request.user,
                is_active=True
            )

        else:
            enrollments = None
    else:
        enrollments = None

    # Form logic
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("accounts:profile")
    else:
        form = ProfileForm(instance=request.user)

    return render(
        request,
        "accounts/profile.html",
        {
            "enrollments": enrollments,
            "form": form,
        },
    )


@login_required
def admin_dashboard(request):
    if not (hasattr(request.user, "userprofile") and request.user.userprofile.role == "admin"):
        messages.error(request, "You do not have permission to access this page.")
        return redirect("accounts:profile")

    return render(request, "accounts/admin.html")
