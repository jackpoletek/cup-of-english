from django.urls import path
from . import views

app_name = "enrollments"

urlpatterns = [
    path("enroll/<int:course_id>/", views.enroll_course, name="enroll_course"),
    path("access/<int:course_id>/", views.access_course, name="access_course"),
]
