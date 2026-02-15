from django.db import models


class Course(models.Model):
    LEVEL_CHOICES = [
        ("A2", "A2"),
        ("B1", "B1"),
        ("B2", "B2"),
        ("C1", "C1"),
        ("C2", "C2"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES, default="A2")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.level})"
