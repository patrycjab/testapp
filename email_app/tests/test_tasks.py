import mock
from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from email_app.tasks import clear_task, save_email, _send_email
from .factories import EmailFactory, StatisticFactory
from smtplib import SMTPException


class SendEmailTest(TestCase):

    @mock.patch("email_app.tasks._send_email")
    def test_should_return_smtpexception(self, send_email):
        # Arrange
        obj_pk = 1
        statistic = StatisticFactory(pk=obj_pk)
        email_obj = EmailFactory(pk=obj_pk)
        send_email.side_effect = SMTPException

        # Act Assert
        with self.assertRaises(SMTPException):
            result = save_email(email_obj.pk)



    def test_should_return_object_doesnot_exist(self):
        # Arrange
        obj_pk = 1
        statistic = StatisticFactory(pk=obj_pk)

        # Act
        result = save_email(obj_pk)

        # Assert
        self.assertEqual(result, None)


class ClearTaskTest(TestCase):

    def test_should_remove_tasks(self):
        # Arrange
        statistics = StatisticFactory(success=120, pk=1)

        # Act
        result = clear_task()

        # Assert
        self.assertEqual(result, None)
