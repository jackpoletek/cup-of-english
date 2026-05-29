from django.db.models import Avg

from enrollments.models import Enrollment
from .models import Course, Review
from .forms import ReviewForm
from enrollments.utils import is_enrolled

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


def courses_view(request):
    """
    Display the main courses page.

    Users can search anf filter available courses by title and level.
    """

    courses = Course.objects.filter(
        is_active=True
    )

    # Search by title
    search_query = request.GET.get("q", "")

    # icontains for case-insensitive search
    if search_query:
        courses = courses.filter(
            title__icontains=search_query
        )

    # Filter by level
    selected_level = request.GET.get("level", "")

    if selected_level:
        courses = courses.filter(
            level=selected_level
        )

    courses = courses.order_by(
        "course_type",
        "level"
    )

    return render(
        request,
        "courses/courses.html",
        {
            "courses": courses,
            "search_query": search_query,
            "selected_level": selected_level,
            "course_type": Course.COURSE_TYPE,
            "levels": [level[0] for level in Course.LEVEL_CHOICES],
        }
    )


def course_list_by_type(request, course_type):
    """
    Show all levels for one selected course type.
    E.G: General English courses of all levels (A2, B1, B2, C1, C2).
    """

    courses = Course.objects.filter(
        is_active=True,
    )

    # Search all courses of the selected type
    search_query = request.GET.get("q", "")

    if search_query:
        courses = courses.filter(
            title__icontains=search_query
        )

    # Filter by level
    selected_level = request.GET.get("level", "")

    if selected_level:
        courses = courses.filter(
            level=selected_level
        )

    # If no search is used, show all courses by type
    if not search_query:
        courses = courses.filter(
            course_type=course_type
        )

    courses = courses.order_by("course_type", "level")

    selected_type = dict(
        Course.COURSE_TYPE
        ).get(course_type, "")

    return render(
        request,
        "courses/course_list.html",
        {
            "courses": courses,
            "selected_type": selected_type,
            "search_query": search_query,
            "selected_level": selected_level,
            "levels": [
                level[0]
                for level in Course.LEVEL_CHOICES],
        }
    )


def course_details(request, course_id):
    """
    Display detailed information about a specific course.
    Also checks if the currently logged-in user is enrolled in this course
    to show relevant enrollment status in the template.
    """

    course = get_object_or_404(
        Course.objects.select_related("teacher"),

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
            "average_rating": average_rating,
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
    ).select_related(
        "course__teacher"
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

    course = get_object_or_404(
        Course.objects.select_related("teacher"),
        id=course_id
    )

    # Check if the user is enrolled in the course
    enrolled = is_enrolled(request.user, course)

    if not enrolled:

        return redirect(
            "courses:course_details",
            course_id=course.id
        )

    return render(
        request,
        "courses/course_content.html",
        {
            "course": course
        }
    )


@login_required
def add_review(request, course_id):
    course = get_object_or_404(
        Course,
        id=course_id
    )

    # Only enrolled learners
    if not is_enrolled(request.user, course):
        return redirect(
            "enrollments:access_denied"
        )

    # Prevent duplicates
    if Review.objects.filter(
        course=course,
        learner=request.user
    ).exists():

        return redirect(
            "courses:course_details",
            course.id
        )

    if request.method == "POST":

        form = ReviewForm(request.POST)

        if form.is_valid():

            review = form.save(commit=False)

            review.course = course
            review.learner = request.user

            review.save()

            return redirect(
                "courses:course_details",
                course_id
            )

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

        return redirect(
            "courses:course_details",
            review.course.id
        )

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
        form = ReviewForm(
            instance=review
        )

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
