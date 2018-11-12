from email_app.forms import EmailForm

from django.test import TestCase
from .factories import EmailFactory


class EmailFormTest(TestCase):

    def test_email_form_valid(self):
        form = EmailForm(data={'title': 'test',
                               'message': 'test_message',
                               'recipient': 'test@test.pl',
                               })
        self.assertTrue(form.is_valid())

    def test_email_form_invalid(self):
        form = EmailForm(data={'title': '',
                               'message': '',
                               'recipient': '',
                               })
        self.assertFalse(form.is_valid())
