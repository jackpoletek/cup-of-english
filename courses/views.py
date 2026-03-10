from django.shortcuts import render


def courses_view(request):
    return render(request, "courses/courses.html")


def home_view(request):
    return render(request, "courses/home.html")
