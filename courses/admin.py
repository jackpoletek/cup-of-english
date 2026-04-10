from django.contrib import admin
from .models import Course


@admin.site.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "level", "course_type", "price", "created_at", "is_active")
