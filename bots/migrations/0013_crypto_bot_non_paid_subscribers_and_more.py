# Generated by Django 4.0.5 on 2022-07-17 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0012_crypto_bot_choose_platform_fx_bot_choose_platform_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='crypto_bot',
            name='non_paid_subscribers',
            field=models.TextField(default='', max_length=10000, verbose_name='Non-Paid Subscribers'),
        ),
        migrations.AddField(
            model_name='crypto_bot',
            name='paid_subscribers',
            field=models.TextField(default='', max_length=10000, verbose_name='Paid Subscribers'),
        ),
        migrations.AddField(
            model_name='fx_bot',
            name='non_paid_subscribers',
            field=models.TextField(default='', max_length=10000, verbose_name='Non-Paid Subscribers'),
        ),
        migrations.AddField(
            model_name='fx_bot',
            name='paid_subscribers',
            field=models.TextField(default='', max_length=10000, verbose_name='Paid Subscribers'),
        ),
        migrations.AddField(
            model_name='gold_bot',
            name='non_paid_subscribers',
            field=models.TextField(default='', max_length=10000, verbose_name='Non-Paid Subscribers'),
        ),
        migrations.AddField(
            model_name='gold_bot',
            name='paid_subscribers',
            field=models.TextField(default='', max_length=10000, verbose_name='Paid Subscribers'),
        ),
        migrations.AddField(
            model_name='indices_bot',
            name='non_paid_subscribers',
            field=models.TextField(default='', max_length=10000, verbose_name='Non-Paid Subscribers'),
        ),
        migrations.AddField(
            model_name='indices_bot',
            name='paid_subscribers',
            field=models.TextField(default='', max_length=10000, verbose_name='Paid Subscribers'),
        ),
    ]