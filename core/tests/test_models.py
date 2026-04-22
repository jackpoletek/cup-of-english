from django.test import TestCase
from core.models import ContactMessage


class ContactMessageModelTest(TestCase):

    def test_create_contact_message(self):
        msg = ContactMessage.objects.create(
            name="John",
            email="john@test.com",
            message="Hello"
        )

        self.assertEqual(msg.name, "John")
        self.assertEqual(str(msg), "John (john@test.com)")
