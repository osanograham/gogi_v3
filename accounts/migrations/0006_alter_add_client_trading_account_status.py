# Generated by Django 4.0.5 on 2022-07-03 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_add_client_trading_account_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_client_trading_account',
            name='status',
            field=models.CharField(choices=[('Deactivate', 'Deactive'), ('Active', 'Active')], max_length=120, verbose_name='Status'),
        ),
    ]