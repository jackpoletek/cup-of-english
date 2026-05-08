from django.contrib import admin
from .models import Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("learner", "course", "get_teacher", "created_at", "is_active")
    search_fields = ("learner__username", "course__title", "course__teacher__username")

    def get_teacher(self, obj):
        # Safely return the teacher's username
        return obj.course.teacher if obj.course.teacher else "No teacher assigned"

    get_teacher.short_description = "Teacher"
