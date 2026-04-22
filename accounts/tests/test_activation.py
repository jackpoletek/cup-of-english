from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes


class ActivationTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@test.com",
            password="pass123",
            is_active=False
        )

    def test_activation_success(self):
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)

        response = self.client.get(
            reverse("accounts:activate", args=[uid, token])
        )

        self.user.refresh_from_db()

        self.assertTrue(self.user.is_active)
        self.assertEqual(response.status_code, 200)

    def test_activation_invalid_token(self):
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))

        response = self.client.get(
            reverse("accounts:activate", args=[uid, "invalid-token"])
        )

        self.user.refresh_from_db()

        self.assertFalse(self.user.is_active)
        self.assertEqual(response.status_code, 200)
