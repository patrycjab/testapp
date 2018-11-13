from datetime import timedelta

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail as _send_email

from celery import task
from celery.decorators import periodic_task

from .models import Email, Statistic
from smtplib import SMTPException

CLEAR_TASK_SENDED = 100


@task(bind=True)
def save_email(self, email_pk):
    statistic = Statistic.objects.get(pk=1)
    try:
        obj = Email.objects.get(id=email_pk)
    except ObjectDoesNotExist:
        return
    email_from = getattr(settings, 'EMAIL_FROM', 'test@task.pl')
    try:
        send = _send_email(
            obj.title,
            obj.message,
            email_from,
            [obj.recipient],
            )
    except SMTPException as e:
        raise self.retry(exc=e)
    else:
        obj.sended = True
        statistic.success = Email.objects.filter(sended=True).count()
    obj.save()
    statistic.errors = Email.objects.filter(sended=False).count()
    statistic.save()


@periodic_task(run_every=timedelta(minutes=15))
def clear_task():
    statistic_succes_obj = Statistic.objects.get(pk=1).success
    if statistic_succes_obj > CLEAR_TASK_SENDED:
        Email.objects.filter(sended=True).delete()
