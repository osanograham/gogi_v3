# Generated by Django 4.0.5 on 2022-07-03 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_add_client_trading_account_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_client_trading_account',
            name='author',
        ),
    ]