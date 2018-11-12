from django.test import TestCase
from email_app.tasks import clear_task, save_email
from .factories import EmailFactory, StatisticFactory

class SendEmailTest(TestCase):

    def test_save_email_success(self):
        statistic = StatisticFactory.build(pk=1)
        email_obj = EmailFactory.create(pk=1)
        result = save_email(1)

    def test_save_email_error(self):
        statistic = StatisticFactory.build(pk=1)
        email_obj = EmailFactory.create(pk=1)
        result = save_email(1)
