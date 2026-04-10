from django.db import models
from django.contrib.auth.models import User
from courses.models import Course


class Enrollment(models.Model):

    """
    Enrollment model represents a learner's registration in a course.
    It tracks which learners are enrolled in which courses,
    which teacher is assigned to the enrollment, and the status of the enrollment.
    It serves as a bridge between the User (learner), Course, and Teacher models.
    """
    # Each enrollment belongs to exactly one learner
    learner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="enrollments",
        )

    # Each enrollment is for exactly one course
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        )

    # Can be null if no teacher is assigned yet, or if teacher is deleted
    teacher = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="teacher_courses",  # Allows user.teacher_courses.all() to get all courses a teacher is teaching
    )

    # Soft delete flag to allow deactivating enrollments without deleting them
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        """
        Meta options for the Enrollment model.
        Defines database constraints and default ordering.
        """
        unique_together = ("learner", "course") # Learner can only be enrolled in a specific course once
        ordering = ["-created_at"]  # Most recent enrollments first (descending order)

    def __str__(self):
        teacher_name = self.teacher.username if self.teacher else "No teacher assigned"
        return f"{self.learner.username} enrolled in {self.course.title} taught by {teacher_name}"
