from django.test import TestCase, Client
from unittest.mock import patch
import json

from django.contrib.auth.models import User
from courses.models import Course
from enrollments.models import Enrollment


class StripeWebhookTest(TestCase):

    def setUp(self):
        self.client = Client()

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

    @patch("stripe.Webhook.construct_event")
    def test_webhook_creates_enrollment(self, mock_construct_event):

        mock_construct_event.return_value = {
            "type": "checkout.session.completed",
            "data": {
                "object": {
                    "metadata": {
                        "user_id": str(self.user.id),
                        "course_id": str(self.course.id)
                    }
                }
            }
        }

        response = self.client.post(
            "/payments/webhook/",
            data=json.dumps({}),
            content_type="application/json",
            HTTP_STRIPE_SIGNATURE="test"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Enrollment.objects.count(), 1)
