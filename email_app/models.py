from django.db import models


class Email(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Tytuł')
    message = models.TextField(verbose_name=u'Treść wiadomości')
    recipient = models.CharField(max_length=500, verbose_name=u'Adresat')
    sended = models.BooleanField(verbose_name=u'Wysłane', default=False)


class Statistic(models.Model):
    success = models.PositiveIntegerField(default=0)
    errors = models.PositiveIntegerField(default=0)
