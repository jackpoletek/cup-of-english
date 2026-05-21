from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from courses.models import Course, Review
from enrollments.models import Enrollment


class CourseViewsTest(TestCase):

    def setUp(self):
        self.course = Course.objects.create(
            title="Test",
            description="Desc",
            level="A2",
            course_type="general",
            price=100
        )

        self.user = User.objects.create_user(
            username="learner",
            password="pass123"
        )

    def test_courses_list(self):
        response = self.client.get(reverse("courses:courses"))
        self.assertEqual(response.status_code, 200)

    def test_course_details(self):
        response = self.client.get(
            reverse(
                "courses:course_details",
                args=[self.course.id]
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_course_list_by_type(self):
        response = self.client.get(
            reverse(
                "courses:course_list_by_type",
                args=["general"]
            )
        )
        self.assertEqual(response.status_code, 200)

        courses = response.context["courses"]
        self.assertEqual(courses.count(), 1)

    def test_enrolled_user_can_add_review(self):
        Enrollment.objects.create(
            learner=self.user,
            course=self.course
        )

        self.client.login(
            username="learner",
            password="pass123"
        )

        response = self.client.post(
            reverse(
                "courses:add_review",
                args=[self.course.id]
            ),
            {
                "rating": 5,
                "comment": "Great course!"
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Review.objects.count(), 1)

    def test_non_enrolled_user_cannot_add_review(self):
        self.client.login(
            username="learner",
            password="pass123"
        )

        response = self.client.post(
            reverse(
                "courses:add_review",
                args=[self.course.id]
            ),
            {
                "rating": 5,
                "comment": "Great course!"
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Review.objects.count(), 0)
