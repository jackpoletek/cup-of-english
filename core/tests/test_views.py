from django.test import TestCase
from django.urls import reverse
from core.models import ContactMessage
from courses.models import Course


class ContactViewTest(TestCase):

    def test_contact_form_submission(self):
        response = self.client.post(
            reverse("core:contact"),
            {
                "name": "John",
                "email": "john@test.com",
                "message": "Test message",
                "captcha": 7,
            }
        )

        self.assertEqual(response.status_code, 302)  # redirect (PRG pattern)
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_contact_form_invalid_captcha(self):
        response = self.client.post(
            reverse("core:contact"),
            {
                "name": "John",
                "email": "john@test.com",
                "message": "Test message",
                "captcha": 5,
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_homepage_displays_one_course_per_category(self):

        Course.objects.create(
            title="General English A2",
            description="Desc",
            level="A2",
            course_type="general",
            price=100,
            is_active=True,
        )

        Course.objects.create(
            title="General English B1",
            description="Desc",
            level="B1",
            course_type="general",
            price=130,
            is_active=True,
        )

        Course.objects.create(
            title="Business English A2",
            description="Desc",
            level="A2",
            course_type="business",
            price=150,
            is_active=True,
        )

        response = self.client.get(reverse("core:index"))

        self.assertEqual(response.status_code, 200)

        featured_courses = response.context["featured_courses"]

        self.assertEqual(len(featured_courses), 2)

        course_types = [
            course.course_type
            for course in featured_courses
        ]

        self.assertEqual(
            sorted(course_types),
            sorted(["general", "business"])
        )
