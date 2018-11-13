import factory
from email_app.models import Email, Statistic
from factory.fuzzy import FuzzyText


class EmailFactory(factory.django.DjangoModelFactory):
    title = FuzzyText(length=20, prefix='tytul_')
    message = FuzzyText(length=20, prefix='message_')
    recipient = 'test@test.pl'
    sended = False

    class Meta:
        model = Email


class StatisticFactory(factory.django.DjangoModelFactory):
    success = 0
    errors = 0

    class Meta:
        model = Statistic
