import mock
from django.test import TestCase

from email_app.models import Email, Statistic
from email_app.tasks import clear_task, save_email

from .factories import EmailFactory, StatisticFactory


class SendEmailTest(TestCase):

    def setUp(self):
        self.obj_pk = 1
        self.statistic = StatisticFactory()

    @mock.patch("email_app.tasks.save_email.retry")
    @mock.patch("email_app.tasks._send_email")
    def test_should_return_smtpexception(self, send_email, retry):
        # Arrange
        expected_count_errors = 1
        email_obj = EmailFactory(pk=self.obj_pk)
        send_email.side_effect = error = Exception()

        # Act
        save_email(email_obj.pk)

        errors_count = Statistic.objects.get(pk=self.obj_pk).errors
        # Assert
        self.assertEqual(errors_count, expected_count_errors)
        retry.assert_called_once_with(exc=error)

    @mock.patch("email_app.tasks.save_email.retry")
    def test_should_return_object_does_not_exist(self, retry):
        # Arrange
        expected_count_errors = 0
        expected_count_success = 0

        # Act
        save_email(self.obj_pk)
        errors_count = Statistic.objects.get(pk=self.obj_pk).errors
        success_count = Statistic.objects.get(pk=self.obj_pk).success

        # Assert
        self.assertEqual(errors_count, expected_count_errors)
        self.assertEqual(success_count, expected_count_success)
        retry.assert_not_called()

    @mock.patch("email_app.tasks.save_email.retry")
    def test_should_return_statistic_success(self, retry):
        # Arrange
        EmailFactory(pk=self.obj_pk)
        expected_count_errors = 0
        expected_count_success = 1

        # Act
        save_email(self.obj_pk)
        errors_count = Statistic.objects.get(pk=self.obj_pk).errors
        success_count = Statistic.objects.get(pk=self.obj_pk).success

        # Assert
        self.assertEqual(errors_count, expected_count_errors)
        self.assertEqual(success_count, expected_count_success)
        retry.assert_not_called()


class ClearTaskTest(TestCase):

    def test_should_remove_tasks(self):
        # Arrange
        StatisticFactory(success=120)
        EmailFactory(sended=True)
        expected_count_emails = 0
        # Act
        clear_task()

        emails_count = Email.objects.all().count()

        # Assert
        self.assertEqual(emails_count, expected_count_emails)
