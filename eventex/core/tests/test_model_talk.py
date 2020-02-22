from django.test import TestCase

from eventex.core.models import Talk


class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title='Talk Title',
        )

    def test_has_speakers(self):
        """Talk has many Speakers and vice-versa"""
        self.talk.speakers.create(
            name='Test Speaker',
            slug='test-speaker',
            photo='http://test-speaker'
        )

        self.talk.speakers.create(
            name='Test Speaker2',
            slug='test-speaker2',
            photo='http://test-speaker2'
        )

        self.assertEqual(2, self.talk.speakers.count())

    def test_create(self):
        self.assertTrue(Talk.objects.exists())

    def test_blank_fields(self):
        fields = [
            'start',
            'description',
            'speakers'
        ]

        for field in fields:
            with self.subTest(self):
                field = self.talk._meta.get_field(field)
                self.assertTrue(field.blank)

    def test_null_fields(self):
        fields = [
            'start',
        ]

        for field in fields:
            with self.subTest(self):
                field = self.talk._meta.get_field(field)
                self.assertTrue(field.blank)

    def test_str(self):
        self.assertEqual(str(self.talk), self.talk.title)
