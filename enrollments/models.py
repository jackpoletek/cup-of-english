from django.db import models
from django.contrib.auth.models import User
from courses.models import Course


class Enrollment(models.Model):

    """
    Enrollment model represents a learner's registration in a course.
    It tracks which learners are enrolled in which courses,
    which teacher is assigned to the enrollment, and the status of the enrollment.
    It serves as a bridge between the User (learner), and Course models.
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

    # Safely get teacher
    def __str__(self):
        teacher_name = (
            self.course.teacher.username
            if self.course.teacher
            else "No teacher assigned"
        )

        return f"{self.learner.username} enrolled in {self.course.title} taught by {teacher_name}"
