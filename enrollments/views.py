from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages

from courses.models import Course
from .models import Enrollment


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

    # Check if user has an active enrollment for the course
    # Using .first() instead of .exists() as we don't need the actual object
    enrollment = Enrollment.objects.filter(
        learner=request.user, course=course, active=True
    ).first()  # Get first matching record or none

    if not enrollment:
        return HttpResponseForbidden(
            "You do not have access to this course."
        )

    return redirect("courses:course_details", course_id=course.id)
