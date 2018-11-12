from django.db import models

# Create your models here.


class Email(models.Model):
    title = models.CharField(max_length=500, verbose_name=u'Tytuł')
    message = models.TextField(verbose_name=u'Treść wiadomości')
    recipient = models.CharField(max_length=500, verbose_name=u'Adresat')


class Statistic(models.Model):
    success = models.PositiveIntegerField(default=0)
    errors = models.PositiveIntegerField(default=0)
