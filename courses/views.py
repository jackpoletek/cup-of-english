from django.db.models import Avg
from urllib3 import request
from urllib3 import request

from enrollments.models import Enrollment
from .models import Course, Review
from .forms import ReviewForm
from enrollments.utils import is_enrolled

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


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
        user_enrolled = is_enrolled(request.user, course)

    average_rating = course.reviews.aggregate(
        Avg("rating")
        )["rating__avg"]

    return render(
        request,
        "courses/course_details.html",
        {
            "course": course,
            "user_enrolled": user_enrolled,
            "average_rating": average_rating
        }
    )


@login_required
def my_courses(request):
    """
    Display all courses the current user is enrolled in.
    """

    # Get access to all active enrollments for the user, along with course and teacher info
    enrollments = Enrollment.objects.filter(
        learner=request.user,
        is_active=True
    ).select_related("course__teacher")

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

    # Check if the user is enrolled in the course
    enrolled = is_enrolled(request.user, course)

    if not enrolled:
        return redirect('courses:course_details', course_id=course.id)

    return render(
        request,
        "courses/course_content.html",
        {
            "course": course
        }
    )


@login_required
def add_review(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    # Only enrolled learners
    if not is_enrolled(request.user, course):
        return redirect("enrollments:access_denied")

    # Prevent duplicates
    if Review.objects.filter(course=course, learner=request.user).exists():
        return redirect("courses:course_details", course_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.course = course
            review.learner = request.user
            review.save()

            return redirect("courses:course_details", course_id)
        
    else:
        form = ReviewForm()

    return render(
        request,
        "courses/add_review.html",
        {
            "form": form,
            "course": course
        }
    )


@login_required
def edit_review(request, review_id):

    review = get_object_or_404(
        Review,
        id=review_id
    )

    # Prevent editing other users reviews
    if review.learner != request.user:
        return redirect("courses:course_details", review.course.id)

    if request.method == "POST":

        form = ReviewForm(
            request.POST,
            instance=review
        )

        if form.is_valid():
            form.save()

            return redirect(
                "courses:course_details",
                review.course.id
            )

    else:
        form = ReviewForm(instance=review)

    return render(
        request,
        "courses/add_review.html",
        {
            "form": form,
            "course": review.course,
            "edit_mode": True,
        }
    )


@login_required
def delete_review(request, review_id):

    review = get_object_or_404(
        Review,
        id=review_id
    )

# Prevent deleting other users reviews
    if review.learner != request.user:
        return redirect("courses:course_details", review.course.id)

    course_id = review.course.id

    review.delete()

    return redirect(
        "courses:course_details",
        course_id
    )
