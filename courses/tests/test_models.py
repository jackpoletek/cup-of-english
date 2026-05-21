from django.test import TestCase
from courses.models import Course, Review
from django.contrib.auth.models import User


class CourseModelTest(TestCase):

    def test_create_course(self):
        course = Course.objects.create(
            title="English",
            description="Desc",
            level="A2",
            course_type="general",
            price=100
        )

        self.assertEqual(str(course), "English")

    def test_review_string_representation(self):
        user = User.objects.create_user(
            username='test',
            password='pass123'
        )

        course = Course.objects.create(
            title="English",
            description="Desc",
            level="A2",
            course_type="general",
            price=100
        )

        review = Review.objects.create(
            learner=user,
            course=course,
            rating=5,
            comment="Great course!"
        )

        self.assertEqual(
            str(review),
            "Test - English (5)"
        )
