from django.contrib import admin
from .models import Course, Review


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "level", "course_type", "price", "is_active",  "created_at")
    search_fields = ("title", "level", "course_type")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("course", "learner", "rating", "created_at")
    search_fields = ("course__title", "learner__username")
