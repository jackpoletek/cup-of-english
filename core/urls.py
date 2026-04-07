from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("teachers/", views.teachers, name="teachers"),
    path("courses/", views.courses, name="courses"),
    path("contact/", views.contact, name="contact"),
]
