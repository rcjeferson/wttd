from django.shortcuts import resolve_url as r
from django.test import TestCase

from eventex.core.models import Speaker, Talk


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

        t1.speakers.add(speaker)
        t2.speakers.add(speaker)

        self.resp = self.client.get(r('talk_list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')

    def test_html(self):
        contents = [
            (1, '10:00'),
            (1, '13:00'),
            (2, '/palestrantes/test-speaker'),
            (2, 'Talk description'),
            (2, 'Test Speaker'),
            (2, 'Talk title'),
        ]

        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

    def test_context(self):
        """Talk must be in context"""
        variables = ['morning_talks', 'afternoon_talks']

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
