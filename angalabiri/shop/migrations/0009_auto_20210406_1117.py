# Generated by Django 3.1.7 on 2021-04-06 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_order_paystack_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='paystack_id',
            new_name='transaction_id',
        ),
    ]
