from django.contrib import admin
from .models import Enrollment


@admin.site.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("learner", "course", "teacher", "created_at", "is_active")
