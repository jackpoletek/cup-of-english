from django.db import models
from django.contrib.auth.models import User
from courses.models import Course


class Enrollment(models.Model):

    """
    Enrollment model represents a learner's registration in a course.
    This model acts as a bridge between:
    - learner (User)
    - course (Course)

    Teacher relationships come from: course.teacher
    This prevents duplicated sources of truth and keeps
    enrollment logic simple.
    """

    # Each enrollment belongs to exactly one learner
    learner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="enrollments",
        )

    # Each enrollment is for exactly one course
    # Enrollments are deleted if the course is deleted
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="enrollments",
    )

    # Soft delete flag to allow deactivating enrollments without deleting them
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:

        """
        Meta options for the Enrollment model.
        Defines database constraints and default ordering.
        """

        # Ensure a learner can only enroll in the same course once
        unique_together = (
            "learner",
            "course"
        )

        # Most recent enrollments first (descending order)
        ordering = [
            "-created_at"
        ]

    # Safely get teacher
    def __str__(self):
        teacher_name = (
            self.course.teacher.username
            if self.course.teacher
            else "No teacher assigned"
        )

        return (
            f"{self.learner.username} enrolled in "
            f"{self.course.title} taught by {teacher_name}"
        )
