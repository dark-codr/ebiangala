# Generated by Django 3.1.7 on 2021-03-23 15:32

import django.contrib.auth.models
from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210322_0202'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('custom', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]