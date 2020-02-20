from django.shortcuts import resolve_url as r
from django.test import TestCase

from eventex.core.models import Speaker


class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Grace Hopper',
            slug='grace-hopper',
            photo='http://hbn.link/hopper-pic',
            website='http://hbn.link/hopper-site',
            description='Programadora e almirante.',
        )

    def test_create(self):
        self.assertTrue(Speaker.objects.exists())

    def test_fields_can_be_blank(self):
        fields = [
            'website',
            'description'
        ]

        for field in fields:
            field = Speaker._meta.get_field(field)
            with self.subTest():
                self.assertTrue(field.blank)

    def test_str(self):
        self.assertEqual('Grace Hopper', str(self.speaker))

    def test_absolute_url(self):
        url = r('speaker_detail', slug=self.speaker.slug)
        self.assertEqual(url, self.speaker.get_absolute_url())
