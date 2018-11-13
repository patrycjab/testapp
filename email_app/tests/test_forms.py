from django.test import TestCase

from email_app.forms import EmailForm


class EmailFormTest(TestCase):

    def test_email_form_valid(self):
        # Arrange
        form = EmailForm(data={'title': 'test',
                               'message': 'test_message',
                               'recipient': 'test@test.pl',
                               })
        # Act
        result = form.is_valid()

        # Assert
        self.assertTrue(result)

    def test_email_form_invalid(self):
        # Arrange
        form = EmailForm(data={'title': '',
                               'message': '',
                               'recipient': '',
                               })
        # Act
        result = form.is_valid()

        # Assert
        self.assertFalse(result)
