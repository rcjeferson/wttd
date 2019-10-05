from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(
            name='Jeferson Costa',
            cpf='12345678901',
            email='email@teste.com',
            phone='99999999999'
        )
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_mail_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_mail_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_mail_to(self):
        expect = ['contato@eventex.com.br', 'email@teste.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_mail_body(self):
        contents = [
            'Jeferson Costa',
            '12345678901',
            'email@teste.com',
            '99999999999',
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
