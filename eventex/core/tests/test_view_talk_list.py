from django.shortcuts import resolve_url as r
from django.test import TestCase

from eventex.core.models import Course, Speaker, Talk


class TalkListGet(TestCase):
    def setUp(self):
        speaker = Speaker.objects.create(
            name='Test Speaker',
            slug='test-speaker',
            photo='http://example.com/pic'
        )

        t1 = Talk.objects.create(
            title='Talk title',
            start='10:00',
            description='Talk description',
        )

        t2 = Talk.objects.create(
            title='Talk title',
            start='13:00',
            description='Talk description',
        )

        c1 = Course.objects.create(
            title='Course title',
            start='09:00',
            description='Course description',
            slots=20
        )

        t1.speakers.add(speaker)
        t2.speakers.add(speaker)
        c1.speakers.add(speaker)

        self.resp = self.client.get(r('talk_list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')

    def test_html(self):
        contents = [
            (1, '09:00'),
            (1, '10:00'),
            (1, '13:00'),
            (1, 'Course description'),
            (1, 'Course title'),
            (2, 'Talk description'),
            (2, 'Talk title'),
            (3, '/palestrantes/test-speaker'),
            (3, 'Test Speaker'),
        ]

        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

    def test_context(self):
        """Talk must be in context"""
        variables = ['talk_list']

        for key in variables:
            with self.subTest():
                self.assertIn(key, self.resp.context)


class TalkListGetEmpty(TestCase):
    def test_get_empty(self):
        response = self.client.get(r('talk_list'))

        self.assertContains(
            response, 'Nenhuma palestra disponível no período da manhã.')
        self.assertContains(
            response, 'Nenhuma palestra disponível no período da tarde.')
