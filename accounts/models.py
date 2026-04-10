from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserProfile(models.Model):
    """
    Extends Django's built-in User model to add role-based functionality.
    Creates a one-to-one relationship with User, allowing each user to have
    a specific role (admin, teacher or learner).
    """

    # Define the available roles as a tuple of tuples
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("teacher", "Teacher"),
        ("learner", "Learner"),
    )

    # One-to-one link to Django's built-in user model
    # Upon user deletion the associated UserProfile will also be deleted (cascade)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        blank=True,
        null=True,
        default=""
    )

    def unique_role(self, new_role):
        """
        Validates if a user can be assigned a new role.
        - Admin cannot change their role
        - Users without a role can take any new role
        - Users can't change their existing role

        Args:
            new_role (str): The role being assigned to the user
        Raises:
            ValidationError: role change is not allowed
        """

        # Admin users do not have role restrictions
        # Admin can be assigned any role
        if self.role == "admin":
            return

        # User has no assignedrole
        # New role matches the existing one
        if not self.role or self.role == new_role:
            return

        raise ValidationError(
            f"You are already registered as {self.role} and cannot register as {new_role}."
        )

    def __str__(self):
        """
        String representation of the UserProfile.        
        Returns:
            str: Format: "username (role)"
        """
        return f"{self.user.username} ({self.role})"
