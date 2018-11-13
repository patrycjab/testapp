from django.test import Client, TestCase

from .factories import EmailFactory


class ViewEmailSendTest(TestCase):

    def test_should_return_status_code_200(self):
        # Arrange
        url = '/'

        # Act
        result = self.client.get(url)

        # Assert
        self.assertEqual(result.status_code, 200)

    def test_should_return_status_code_302(self):
        # Arrange
        url = '/'
        data = {'title': 'test',
                'message': 'test_message',
                'recipient': 'test@test.pl'}

        # Act
        result = self.client.post(url, data)

        # Assert
        self.assertEqual(result.status_code, 302)
        self.assertEqual(result.url, url)
