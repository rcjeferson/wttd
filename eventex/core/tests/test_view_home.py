from django.shortcuts import resolve_url as r
from django.test import TestCase


class HomeTest(TestCase):
    fixtures = ['keynotes.json']

    def setUp(self):
        self.resp = self.client.get(r('home'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_subscription_link(self):
        expected = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.resp, expected)

    def test_speakers(self):
        """Must show keynote speakers"""
        content = [
            'href="{}"'.format(r('speaker_detail', slug='grace-hopper')),
            'Grace Hopper',
            'http://hbn.link/hopper-pic',
            'href="{}"'.format(r('speaker_detail', slug='alan-turing')),
            'Alan Turing',
            'http://hbn.link/turing-pic',
        ]

        for expected in content:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_anchor_links(self):
        """Must has specified anchor links in menu"""
        expected = [
            'overview',
            'speakers',
            'sponsors',
            'register',
            'venue',
        ]

        for link in expected:
            with self.subTest():
                self.assertContains(self.resp, '{}#{}'.format(r('home'), link))

    def test_url_links(self):
        """Must has specified url links in menu"""
        expected = [
            r('talk_list')
        ]

        for url in expected:
            with self.subTest():
                self.assertContains(self.resp, 'href="{}"'.format(url))
