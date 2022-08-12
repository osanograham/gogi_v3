# Generated by Django 4.0.5 on 2022-07-03 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_add_client_trading_account_account_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_client_trading_account',
            name='status',
            field=models.CharField(choices=[('Deactivate', 'Deactive'), ('Active', 'Active')], default='Deactive', max_length=120, verbose_name='Status'),
        ),
    ]
