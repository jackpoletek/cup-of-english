from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "level", "course_type", "price", "created_at", "is_active")
    search_fields = ("title", "level", "course_type")
