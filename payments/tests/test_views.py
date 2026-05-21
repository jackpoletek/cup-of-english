from unittest.mock import patch, MagicMock
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from courses.models import Course


class PaymentTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            password="pass123"
        )

        self.course = Course.objects.create(
            title="Test",
            description="Desc",
            level="A2",
            course_type="general",
            price=100
        )

    def test_checkout_requires_login(self):
        response = self.client.get(
            reverse("payments:checkout", args=[self.course.id])
        )

        self.assertEqual(response.status_code, 302)

    def test_payment_success_page(self):
        response = self.client.get("/payments/success/")
        self.assertEqual(response.status_code, 200)

    def test_payment_cancel_page(self):
        response = self.client.get("/payments/cancel/")
        self.assertEqual(response.status_code, 200)

    @patch("payments.views.stripe.checkout.Session.create")
    def test_checkout_redirects_for_non_learner(
        self,
        mock_session_create
    ):

        self.client.login(
            username="test",
            password="pass123"
        )

        response = self.client.get(
            reverse("payments:checkout", args=[self.course.id])
        )

        self.assertEqual(response.status_code, 302)
        mock_session_create.assert_not_called()

    @patch("payments.views.stripe.checkout.Session.create")
    def test_checkout_creates_stripe_session(
        self,
        mock_session_create
    ):

        self.user.profile.role = "learner"
        self.user.profile.save()

        mock_session = MagicMock()
        mock_session.url = "/fake-checkout-url/"

        mock_session_create.return_value = mock_session

        self.client.login(
            username="test",
            password="pass123"
        )

        response = self.client.get(
            reverse("payments:checkout", args=[self.course.id])
        )

        self.assertEqual(response.status_code, 302)

        mock_session_create.assert_called_once()
