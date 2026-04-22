from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class AuthTests(TestCase):

    def test_register(self):
        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "user1",
                "email": "user@test.com",
                "password": "testpass123",
                "password_again": "testpass123",
                "role": "learner"
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)

    def test_login(self):
        user = User.objects.create_user(
            username="test",
            password="pass123",
            is_active=True
        )

        response = self.client.post(
            reverse("accounts:login"),
            {
                "username": "test",
                "password": "pass123"
            }
        )

        self.assertEqual(response.status_code, 302)

    def test_login_blocked_if_not_active(self):
        user = User.objects.create_user(
            username="inactive",
            password="pass123",
            is_active=False
        )

        response = self.client.post(
            reverse("accounts:login"),
            {
                "username": "inactive",
                "password": "pass123"
            }
        )

        self.assertEqual(response.status_code, 200)
