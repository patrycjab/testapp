from datetime import timedelta

from django.conf import settings
from django.core.mail import send_mail as _send_email

from celery import shared_task
from celery.decorators import periodic_task

from .models import Email, Statistic


@shared_task(max_retries=2)
def save_email(email_pk):
    statistic = Statistic.objects.get_or_create(pk=1)[0]
    try:
        obj = Email.objects.get(id=email_pk)
    except ObjectDoesNotExist:
        pass
    if obj:
        email_from = getattr(settings, 'EMAIL_FROM', 'test@task.pl')
        try:
            send = _send_email(
                obj.title,
                obj.message,
                email_from,
                [obj.recipient],
                )
        except Exception:
            obj.sended = False
        else:
            obj.sended = True
        obj.save()
        statistic.errors = Email.objects.filter(sended=False).count()
        statistic.success = Email.objects.filter(sended=True).count()
        statistic.save()

@periodic_task(run_every=timedelta(minutes=15))
def clear_task():
    statistic_succes_obj = Statistic.objects.get(pk=1).success
    if statistic_succes_obj > 100:
        Email.objects.filter(sended=True).delete()

