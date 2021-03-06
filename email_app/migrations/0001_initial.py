# Generated by Django 2.1.3 on 2018-11-13 21:30

from django.db import migrations, models

def create_statistic(apps, schema_editor):
    Statistic = apps.get_model("email_app", "Statistic")
    Statistic.objects.bulk_create([
        Statistic(success=0, errrors=0)])


def create_statistic(apps, schema_editor):
    Statistic = apps.get_model("email_app", "Statistic")
    Statistic.objects.bulk_create([
        Statistic(success=0, errors=0)])


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Tytuł')),
                ('message', models.TextField(verbose_name='Treść wiadomości')),
                ('recipient', models.CharField(max_length=500, verbose_name='Adresat')),
                ('sended', models.BooleanField(default=False, verbose_name='Wysłane')),
            ],
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success', models.PositiveIntegerField(default=0)),
                ('errors', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RunPython(create_statistic),
    ]
