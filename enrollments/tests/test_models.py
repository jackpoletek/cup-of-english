from django.test import TestCase
from django.contrib.auth.models import User
from courses.models import Course
from enrollments.models import Enrollment


class EnrollmentModelTest(TestCase):

    def test_create_enrollment(self):
        user = User.objects.create_user(username="u", password="p")
        course = Course.objects.create(
            title="Test",
            description="Desc",
            level="A2",
            course_type="general",
            price=100
        )

        enrollment = Enrollment.objects.create(
            learner=user,
            course=course
        )

        self.assertEqual(enrollment.learner, user)
