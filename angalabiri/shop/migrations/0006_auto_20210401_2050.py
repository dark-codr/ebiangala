# Generated by Django 3.1.7 on 2021-04-01 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210401_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='inventory',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
