# Generated by Django 3.2.8 on 2021-10-18 21:24

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Checkbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
                ('Accounts', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='transaction',
            managers=[
                ('Transaction', django.db.models.manager.Manager()),
            ],
        ),
    ]
