from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from enrollments.models import Enrollment
from .models import Course


def courses_view(request):
    """
    Display a list of all active courses available.

    This view filters courses to show only those marked as active.

    Args:
        request: HTTP request object

    Returns:
        Rendered template with active courses
    """

    courses = Course.objects.filter(is_active=True)

    return render(
        request,
        "courses/courses.html",
        {
            "courses": courses
        }
    )


def course_details(request, course_id):
    """
    Display detailed information about a specific course.

    Also checks if the currently logged-in user is enrolled in this course
    to show relevant enrollment status/actions in the template.

    Args:
        request: HTTP request object
        course_id: Primary key of the course to display

    Returns:
        Rendered template with course details and enrollment status
    """

    # This handles both non-existent and inactive courses
    course = get_object_or_404(Course, id=course_id)

    user_enrolled = False

    if request.user.is_authenticated:
        # Check for active enrollment for this user and course
        # exists() returns True if at least one matching record is found

        user_enrolled = Enrollment.objects.filter(
            learner=request.user,
            course=course,
            is_active=True
        ).exists()

    return render(
        request,
        "courses/course_details.html",
        {
            "course": course,
            "user_enrolled": user_enrolled
        }
    )


@login_required
def my_courses(request):
    """
    Display all courses the current user is enrolled in.

    This is a personalised view showing the user's learning dashboard.
    Requires authentication (@login_required decorator).

    Args:
        request: HTTP request object (user is guaranteed to be authenticated)

    Returns:
        Rendered template with user's active enrollments
    """

    # Get all active enrollments for the current user
    enrollments = Enrollment.objects.filter(
        learner=request.user,
        is_active=True
    )

    return render(
        request,
        "courses/my_courses.html",
        {
            "enrollments": enrollments
        }
    )
