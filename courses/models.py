from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    """
    Course model representing English language courses offered on the platform.

    This model stores all course-related information including title, description,
    difficulty level, type, pricing, and availability status.
    """

    LEVEL_CHOICES = (
        ("A2", "A2"),
        ("B1", "B1"),
        ("B2", "B2"),
        ("C1", "C1"),
        ("C2", "C2"),
    )

    COURSE_TYPE = (
        ("general", "General English"),
        ("business", "Business English"),
        ("exam", "Exam Preparation"),
        ("esp", "English for Specific Purposes"),
    )

    title = models.CharField(max_length=255)

    description = models.TextField()

    level = models.CharField(
        max_length=2,
        choices=LEVEL_CHOICES
    )

    course_type = models.CharField(
        max_length=20,
        choices=COURSE_TYPE
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title
