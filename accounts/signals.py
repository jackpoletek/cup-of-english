from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler automatically creates a UserProfile when a new user is created.
    This is triggered after a user instance is saved to the database.
    It ensures every user has a profile for role management.

    Args:
        sender: The model class (User) that sent the signal
        instance: The actual User instance being saved
        created: Boolean flag - True if a new user has been created, False if updated
        **kwargs: Additional keyword arguments from the signal
    """

    # Only create a profile for new users
    if created:
        # get_or_create prevents duplicates if user already exists
        UserProfile.objects.get_or_create(user=instance)



@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal handler automatically saves UserProfile when a user is saved.
    This ensures the profile is always updated when the user instance is saved.

    Args:
        sender: The model class (User) that sent the signal
        instance: The actual User instance being saved
        **kwargs: Additional arguments
    """
    try:
        instance.userprofile.save()
    except AttributeError:
        pass
