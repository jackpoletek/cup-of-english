from django.shortcuts import render


def course_list(request):
    """
    Display courses page.
    """
    return render(request, "courses/courses.html")
