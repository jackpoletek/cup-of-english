from teachers.models import TeacherProfile
from teachers.forms import TeacherProfileForm

import logging
import time

from collections import defaultdict

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
                messages.info(
                    request,
                    "Account already activated. You can now log in."
                )
                return redirect("accounts:login")

            last_sent = request.session.get(
                "last_activation_email_sent",
                0
            )
            now = time.time()

            if now - last_sent < 60:  # 1 minute cooldown
                messages.error(
                    request,
                    "Activation email was sent. Please wait before requesting again."
                )
                return redirect("accounts:login")

            send_activation_email(user, request)

            request.session["last_activation_email_sent"] = now

            messages.success(
                request,
                "Activation email resent successfully."
            )

        except User.DoesNotExist:
            messages.error(
                request,
                "No account found with this email."
            )

        except Exception:
            # Log the error but avoid leaking information to the user

            logger.exception("Error resending activation email.")

            messages.error(
                request,
                "Resending activation email failed. Please try again later."
            )

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

        # Send activation email
        try:
            send_activation_email(user, request)

        except Exception:
            messages.warning(
                request,
                "Account created but failed to send activation email."
            )

            return redirect("accounts:login")

        messages.success(
            request,
            "Account created. Check your email to activate your account."
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

            # Activate the user if not already active
            if not user.is_active:
                user.is_active = True
                user.save()

            return render(
                request,
                "accounts/activation_success.html"
            )

        return render(
            request,
            "accounts/activation_failed.html"
        )

    except Exception:
        return render(request, "accounts/activation_failed.html")


# Authenticated views
@login_required
def profile(request):

    user = request.user

    enrollments = []

    # Build mapping of teachers to their courses
    teachers_courses = {}

    teacher_profile = None
    teacher_form = None

    # Only show enrollments if user has a profile with a valid role
    if hasattr(user, "userprofile"):

        if user.userprofile.role == "learner":

            enrollments = Enrollment.objects.filter(
                learner=user,
                is_active=True  # Only show active enrollments
            )

        elif user.userprofile.role == "teacher":

            teacher_courses = user.teaching_courses.all()  # Get all courses taught by this teacher

            teacher_enrollments = Enrollment.objects.filter(
                teacher=user,
                is_active=True  # Only show active enrollments
            ).select_related(
                "learner",
                "course"
            )

            teachers_courses = defaultdict(list)

            # Display enrollments grouped by course for teachers
            for enrollment in teacher_enrollments:
                teachers_courses[enrollment.course].append(enrollment)

            teachers_courses = dict(teachers_courses)  # Convert back to regular dict for template

            # Get or create teacher profile for the form
            teacher_profile, created = TeacherProfile.objects.get_or_create(
                user=user
            )

    if request.method == "POST":

        # Teacher profile form handling
        if (
            hasattr(user, "userprofile")
            and user.userprofile.role == "teacher"
            and "teacher_profile_submit" in request.POST
        ):

            teacher_profile, created = TeacherProfile.objects.get_or_create(
                user=user
            )

            teacher_form = TeacherProfileForm(
                request.POST,
                request.FILES,
                instance=teacher_profile
            )

            if teacher_form.is_valid():

                if "delete_image" in request.POST:

                    if teacher_profile.image:
                        teacher_profile.image.delete(save=False)  # Delete the file but keep the model instance

                    teacher_profile.image = None  # Clear the image field

                teacher_form.save()

                messages.success(
                    request,
                    "Teacher profile updated successfully."
                )

                return redirect("accounts:profile")

        else:

            form = ProfileForm(
                request.POST,
                instance=user
            )

            # Only allow saving if form is valid
            if form.is_valid():
                form.save()

                messages.success(
                    request,
                    "Profile updated successfully."
                )

                return redirect("accounts:profile")

    else:
        form = ProfileForm(instance=user)

        if (
            hasattr(user, "userprofile")
            and user.userprofile.role == "teacher"
        ):
            teacher_form = TeacherProfileForm(
                instance=teacher_profile
            )

    return render(
        request,
        "accounts/profile.html",
        {
            "form": form,
            "enrollments": enrollments,
            "teachers_courses": teachers_courses,
            "teacher_form": teacher_form,
            "teacher_profile": teacher_profile,
        }
    )


@login_required
def admin_dashboard(request):
    if not (
        hasattr(request.user, "userprofile")
            and request.user.userprofile.role == "admin"
    ):
        messages.error(
            request,
            "You do not have permission to access this page."
        )

        return redirect("accounts:profile")

    return render(request, "accounts/admin.html")
