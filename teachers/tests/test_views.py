from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import UserProfile


class TeacherViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="teacher",
            password="pass123"
        )
        self.user.userprofile.role = "teacher"
        self.user.userprofile.save()

    def test_teacher_list(self):
        response = self.client.get(reverse("teachers"))
        self.assertEqual(response.status_code, 200)
