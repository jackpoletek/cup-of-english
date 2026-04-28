from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from enrollments.models import Enrollment
from .models import Course


def courses_view(request):
    """
    Display the main courses page.

    For simplicity, this page is intentionally static
    and showcases the 6 core course categories without database dependency.

    Actual purchasable courses are displayed only after selecting
    a category via course_list_by_type.
    """

    return render(
        request,
        "courses/courses.html"
    )


def course_list_by_type(request, course_type):
    """
    Show all levels for one selected course type.
    E.G: General English courses of all levels (A2, B1, B2, C1, C2).
    """
    courses = Course.objects.filter(
        is_active=True,
        course_type=course_type
    ).order_by("level")

    return render(
        request,
        "courses/course_list.html",
        {
            "courses": courses,
            "selected_type": courses.first().get_course_type_display() if courses else ""
        }
    )


def course_details(request, course_id):
    """
    Display detailed information about a specific course.
    Also checks if the currently logged-in user is enrolled in this course
    to show relevant enrollment status in the template.
    """

    course = get_object_or_404(
        Course,
        id=course_id,
        is_active=True
    )

    user_enrolled = False

    if request.user.is_authenticated:
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
    """

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


@login_required
def course_content(request, course_id):
    """
    Display the content of a specific course for enrolled users.
    """

    course = get_object_or_404(Course, id=course_id)

    is_enrolled = Enrollment.objects.filter(
        learner=request.user,
        course=course,
        is_active=True
    ).exists()

    if not is_enrolled:
        return redirect('courses:course_details', course_id=course.id)

    return render(
        request,
        "courses/course_content.html",
        {
            "course": course
        }
    )
