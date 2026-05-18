from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("", views.courses_view, name="courses"),
    path("my-courses/", views.my_courses, name="my_courses"),

    path(
        "type/<str:course_type>/",
        views.course_list_by_type,
        name="course_list_by_type"
    ),

    path(
        "<int:course_id>/",
        views.course_details,
        name="course_details"
        ),

    path(
        "<int:course_id>/content/",
        views.course_content,
        name="course_content"
        ),

    path(
        "course/<int:course_id>/review/",
        views.add_review,
        name="add_review"
        ),

    path(
        "review/<int:review_id>/edit/",
        views.edit_review,
        name="edit_review"
        ),

    path(
        "review/<int:review_id>/delete/",
        views.delete_review,
        name="delete_review"
        ),
]
