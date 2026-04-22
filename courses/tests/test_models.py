from django.test import TestCase
from courses.models import Course


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
