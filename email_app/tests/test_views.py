from django.test import Client, TestCase

from .factories import EmailFactory


class ViewEmailSendTest(TestCase):

    def test_should_return_status_code_200(self):
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)

    def test_should_return_status_code_302(self):
        data = {'title': 'test',
                'message': 'test_message',
                'recipient': 'test@test.pl'}
        result = self.client.post('/', data)
        self.assertEqual(result.status_code, 302)

