from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from courses.models import Course


class EnrollmentViewsTest(TestCase):

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

    def test_enroll_requires_login(self):
        response = self.client.get(
            reverse("enrollments:enroll_course", args=[self.course.id])
        )
        self.assertEqual(response.status_code, 302)

    def test_enroll_logged_in(self):
        self.client.login(username="test", password="pass123")

        response = self.client.get(
            reverse("enrollments:enroll_course", args=[self.course.id])
        )

        self.assertEqual(response.status_code, 302)
