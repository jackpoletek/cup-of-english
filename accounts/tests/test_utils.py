from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User

from accounts.utils import generate_activation_link


class UtilsTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get("/")
        self.user = User.objects.create_user(
            username="test",
            email="test@test.com",
            password="pass123"
        )

    def test_activation_link_generation(self):
        link = generate_activation_link(self.request, self.user)

        self.assertIn("activate", link)
        self.assertIn(str(self.user.pk), link)
