import factory
from email_app.models import Email, Statistic
from factory.fuzzy import FuzzyText


class EmailFactory(factory.Factory):
    title = FuzzyText(length=20, prefix='tytul_')
    message = FuzzyText(length=20, prefix='message_')
    recipient = 'test@test.pl'

    class Meta:
        model = Email


class StatisticFactory(factory.Factory):
    success = 0
    errors = 0

    class Meta:
        model = Statistic
