from datetime import timedelta

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail as _send_email

from celery import task
from celery.decorators import periodic_task

from .models import Email, Statistic

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
        _send_email(
            obj.title,
            obj.message,
            email_from,
            [obj.recipient],
            )
    except Exception as e:
        statistic.errors = Email.objects.filter(sended=False).count()
        self.retry(exc=e)
    else:
        obj.sended = True
        obj.save()
        statistic.success = Email.objects.filter(sended=True).count()
    finally:
        statistic.save()


@periodic_task(run_every=timedelta(minutes=15))
def clear_task():
    success_email_sended = Statistic.objects.get(pk=1).success
    if success_email_sended > CLEAR_TASK_SENDED:
        Email.objects.filter(sended=True).delete()
    return
