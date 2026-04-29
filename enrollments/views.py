from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from courses.models import Course
from .models import Enrollment
from enrollments.utils import is_enrolled


@login_required
def enroll_course(request, course_id):
    """
    Handle course enrollment for authenticated learners.
    This view allows authenticated users to enroll in a course.
    It prevents duplicate enrollments and provides appropriate feedback messages.

    Args:
        request: HTTP request object (user is guaranteed authenticated)
        course_id: Primary key of the course to enroll in
    Returns:
        Redirect to course detail page with appropriate status message
    """

    course = get_object_or_404(Course, id=course_id)

    enrollment, created = Enrollment.objects.get_or_create(
        learner=request.user,
        course=course
    )

    if not created:
        messages.info(request, "You are already enrolled in this course.")

    else:
        messages.success(request, "Enrollment successful.")

    return redirect("courses:course_details", course_id=course.id)


@login_required
def access_course(request, course_id):

    course = get_object_or_404(Course, id=course_id)

    # Check enrollment status and show access denied page if not enrolled, otherwise redirect to course details
    if not is_enrolled(request.user, course):
        return render(
            request,
            "enrollments/access_denied.html",
        )

    return redirect("courses:course_details", course_id=course.id)
