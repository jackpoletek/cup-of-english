from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import UserProfile


class UserProfileModelTest(TestCase):

    def test_profile_created(self):
        user = User.objects.create_user(
            username="test",
            password="pass123"
        )

        self.assertTrue(hasattr(user, "userprofile"))
