from django.db import models
from django.contrib.auth.models import User
from courses.models import Course


class Enrollment(models.Model):
    learner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="enrollments",
        )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="enrollments",
        )
    teacher = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="teaching_assignments",
        )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.learner.username} enrolled in {self.course.title} taught by {self.teacher.username}"
