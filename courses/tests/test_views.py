from django.test import TestCase
from django.urls import reverse
from courses.models import Course


class CourseViewsTest(TestCase):

    def setUp(self):
        self.course = Course.objects.create(
            title="Test",
            description="Desc",
            level="A2",
            course_type="general",
            price=100
        )

    def test_courses_list(self):
        response = self.client.get(reverse("courses:courses"))
        self.assertEqual(response.status_code, 200)

    def test_course_details(self):
        response = self.client.get(
            reverse("courses:course_details", args=[self.course.id])
        )
        self.assertEqual(response.status_code, 200)
