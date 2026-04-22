from django.test import TestCase
from django.urls import reverse
from core.models import ContactMessage


class ContactViewTest(TestCase):

    def test_contact_form_submission(self):
        response = self.client.post(
            reverse("core:contact"),
            {
                "name": "John",
                "email": "john@test.com",
                "message": "Test message"
            }
        )

        self.assertEqual(response.status_code, 302)  # redirect (PRG pattern)
        self.assertEqual(ContactMessage.objects.count(), 1)
