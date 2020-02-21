from django.core.exceptions import ValidationError
from django.test import TestCase

from eventex.core.models import Contact, Speaker


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Grace Hopper',
            slug='grace-hopper',
            photo='http://hbn.link/hopper-pic',
        )

        self.contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='grace@hopper.com',
        )

    def test_create(self):
        self.assertTrue(Contact.objects.exists())

    def test_email(self):
        Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='grace@hopper.com',
        )

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='19999999999',
        )

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind must be limited to E or P"""
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind='A',
            value='B',
        )

        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        self.assertEqual(str(self.contact), self.contact.value)
