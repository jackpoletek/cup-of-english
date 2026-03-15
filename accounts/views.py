from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.db import OperationalError
import logging

from .models import UserProfile

# Logger to track errors and events
logger = logging.getLogger(__name__)


# Role helper function
def user_is_teacher(user):
    """
    Check if a user has the teacher role.

    Returns:
        bool: True if user has a profile with role='teacher', False otherwise
    """
    # hasattr safely checks if profile exists before accessing role
    return hasattr(user, "userprofile") and user.userprofile.role == "teacher"

def user_is_learner(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "learner"


# Authentication views
def login_view(request):
    """
    Handle user login.

    GET: Display login form
    POST: Authenticate user and redirect to profile if successful

    Includes error handling for database unavailability.
    """
    # If user is already authenticated, redirect to profile
    if request.user.is_authenticated:
        return redirect("accounts:profile")

    if request.method == "GET":
        return render(request, "accounts/login.html")

    try:

        username = request.POST.get("username").strip()
        password = request.POST.get("password").strip()

        if not username or not password:
            return render(
                request,
                "accounts/login.html",
                {
                    "login_error": True,
                    "error_message": "Username and password are required.",
                },
                status=400,
            )

        user = authenticate(request, username=username, password=password)

        if user is not None:
            return render(
                request,
                "accounts/login.html",
                {
                    "login_error": True,
                    "error_message": "Invalid username or password.",
                },
                status=401,
            )

        auth_login(request, user)

        return redirect("accounts:profile")

    except OperationalError as e:

        logger.exception("Database error during login: %s", e)

        return render(
            request,
            "accounts/login.html",
            {
                "login_error": True,
                "error_message": "System is temporarily unavailable. Please try again later.",
            },
            status=503,
        )


def logout_view(request):
    """
    Log out the current user and redirect to homepage.
    If the user is not authenticated, simply redirect to homepage.
    """
    if request.user.is_authenticated:
        auth_logout(request)

    return redirect("core:index")


def register_view(request):
    """
    Handle new user registration.

    GET: Display registration form
    POST: Create new user account with role

    Validation for:
    - Required fields
    - Valid role selection
    - Password confirmation
    - Unique username and email
    """
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

        if not all([username, email, password, password_again, role]):

            return render(
                request,
                "accounts/register.html",
                {
                    "registration_error": True,
                    "error_message": "All fields are required.",
                },
            )

        if role not in ["teacher", "learner"]:

            return render(
                request,
                "accounts/register.html",
                {
                    "registration_error": True,
                    "error_message": "Please select a valid role.",
                },
            )

        if password != password_again:

            return render(
                request,
                "accounts/register.html",
                {
                    "registration_error": True,
                    "error_message": "Passwords do not match.",
                },
            )

        if User.objects.filter(username=username).exists():

            return render(
                request,
                "accounts/register.html",
                {
                    "registration_error": True,
                    "error_message": "Username already exists.",
                },
            )

        if User.objects.filter(email=email).exists():
            return render(
                request,
                "accounts/register.html",
                {
                    "registration_error": True,
                    "error_message": "Email already in use.",
                },
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        profile = user.profile
        profile.role = role
        profile.save()

        return render(
            request,
            "accounts/register.html",
            {
                "registration_success": True,
                "success_message": "Account created successfully! You can now log in.",
            },
        )

    except OperationalError:

        logger.exception("Database error during registration")

        return render(
            request,
            "accounts/register.html",
            {
                "registration_error": True,
                "error_message": "System is temporarily unavailable. Please try again later.",
            },
            status=503,
        )


# Decorator ensures only authenticated users can access the profile view
@login_required
def profile(request):
    """
    Display user profile page.
    Requires authentication - decorator will redirect unauthenticated users to login page.
    """
    return render(
        request,
        "accounts/profile.html"
    )
