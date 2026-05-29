from django.contrib import admin
from .models import Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("learner", "course", "created_at", "is_active")
    search_fields = ("learner__username", "course__title")

    fields = ("learner", "course", "is_active")
    readonly_fields = ("created_at",)
