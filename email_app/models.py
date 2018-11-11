from django.db import models

# Create your models here.


class Email(models.Model):
    title = models.CharField(max_length=500, verbose_name=u'Tytuł')
    message = models.TextField(verbose_name=u'Treść wiadomości')
    recipient = models.CharField(max_length=500, verbose_name=u'Nadawca')
