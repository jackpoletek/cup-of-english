from django.db import models
from django.contrib.auth.models import User


def teacher_image_path(instance, filename):
    return f"teachers/{instance.user.username}/{filename}"


class TeacherProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
        )

    bio = models.TextField(
        max_length=500,
        blank=True)

    image = models.ImageField(
        upload_to=teacher_image_path,
        blank=True,
        null=True)

    def __str__(self):
        return self.user.username
