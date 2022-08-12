# Generated by Django 4.0.5 on 2022-07-16 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0011_add_client_trading_account_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_client_trading_account',
            name='created_by',
            field=models.ForeignKey(default='', max_length=156, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]