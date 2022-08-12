# Generated by Django 4.0.5 on 2022-07-15 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0010_crypto_bot'),
    ]

    operations = [
        migrations.AddField(
            model_name='crypto_bot',
            name='instruments',
            field=models.CharField(default='', max_length=150, verbose_name='Instruments'),
        ),
        migrations.AddField(
            model_name='fx_bot',
            name='instruments',
            field=models.CharField(default='', max_length=150, verbose_name='Instruments'),
        ),
        migrations.AddField(
            model_name='gold_bot',
            name='instruments',
            field=models.CharField(default='', max_length=150, verbose_name='Instruments'),
        ),
    ]