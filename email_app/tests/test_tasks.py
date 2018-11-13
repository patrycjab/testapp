from django.test import TestCase
from email_app.tasks import clear_task, save_email
from .factories import EmailFactory, StatisticFactory


class SendEmailTest(TestCase):

    def test_save_email_success(self):
        # Arrange
        email_pk = 1
        import ipdb;ipdb.set_trace()
        statistic = StatisticFactory()
        email_obj = EmailFactory()

        # Act
        result = save_email(email_obj.pk)

        # Assert
        self.assertEqual(result, 'ok')

    def test_save_email_error(self):
        # Arrange
        email_pk = 1
        statistic = StatisticFactory.build(pk=1)

        # Act
        result = save_email(email_pk)

        # Assert
        self.assertEqual(result, None)
