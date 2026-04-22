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
