from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("", views.courses_view, name="courses"),
]
