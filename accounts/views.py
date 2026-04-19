import logging

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import OperationalError, transaction, IntegrityError

from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

from .utils import generate_activation_link

from .forms import ProfileForm
from enrollments.models import Enrollment
from .models import UserProfile

logger = logging.getLogger(__name__)


# Role helpers
def user_is_teacher(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "teacher"


def user_is_learner(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "learner"


# Login
def login_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:profile")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        if not username or not password:
            messages.error(request, "Both fields are required.")
            return render(request, "accounts/login.html")

        user = authenticate(request, username=username, password=password)

        # Block login if email not verified
        if user is not None:
            if not user.is_active:
                messages.error(request, "Please verify your email address first.")
                return render(request, "accounts/login.html")

            auth_login(request, user)
            return redirect("accounts:profile")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")


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
        activation_link = generate_activation_link(request, user)

        send_mail(
            subject="Activate your account",
            message=f"Please click the link to activate your account:\n{activation_link}",
            from_email="gr8tutorjack@gmail.com",
            recipient_list=[email],
            fail_silently=False,  # Log email sending issues
        )

        messages.success(request, "Account created successfully. Please log in.")
        return redirect("accounts:login")

    except IntegrityError:
        logger.exception("Error during registration.")
        messages.error(request, "Registration failed. Please try again later.")
        return render(request, "accounts/register.html")

    except OperationalError:
        logger.exception("Database error during registration.")
        messages.error(request, "System is temporarily unavailable. Please try again later.")
        return render(request, "accounts/register.html", status=503)


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
