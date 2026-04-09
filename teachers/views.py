from django.shortcuts import render
from django.contrib.auth.models import User

from accounts.models import UserProfile

def teacher_list(request):

    teachers = UserProfile.objects.filter(role="teacher").select_related("user")

    return render(
        request,
        "teachers/teachers.html",
        {
            "teachers": teachers
        },
    )
