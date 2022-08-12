# Generated by Django 4.0.5 on 2022-06-27 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='add_client_trading_account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(blank=True, max_length=50, verbose_name='Account_Name')),
                ('choose_platform', models.CharField(choices=[('MT4', 'MT4'), ('MT5', 'MT5')], default='MT4', max_length=50, verbose_name='Platform')),
                ('account_number', models.CharField(max_length=300, verbose_name='Account_Number')),
                ('account_password', models.CharField(max_length=300, verbose_name='password')),
                ('account_server_name', models.CharField(max_length=100, verbose_name='Account Server Name')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date Added')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
