from django.test import TestCase
from django.urls import reverse


class ViewEmailSendTest(TestCase):

    def test_should_return_status_code_200(self):

        # Act
        result = self.client.get(reverse('my-site'))

        # Assert
        self.assertEqual(result.status_code, 200)

    def test_should_return_status_code_302(self):
        # Arrange
        data = {'title': 'test',
                'message': 'test_message',
                'recipient': 'test@test.pl'}

        # Act
        result = self.client.post(reverse('my-site'), data)

        # Assert
        self.assertEqual(result.status_code, 302)
        self.assertEqual(result.url, reverse('my-site'))
