from django.shortcuts import render


def teacher_list(request):
    return render(request, "teachers/teachers.html")
