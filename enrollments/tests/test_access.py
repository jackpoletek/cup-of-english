from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from courses.models import Course


class AccessControlTest(TestCase):

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

    def test_access_denied_if_not_enrolled(self):
        self.client.login(username="test", password="pass123")

        response = self.client.get(
            reverse("courses:course_content", args=[self.course.id])
        )

        self.assertEqual(response.status_code, 302)
