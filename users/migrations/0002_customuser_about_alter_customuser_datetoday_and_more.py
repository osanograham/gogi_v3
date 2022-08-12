# Generated by Django 4.0.5 on 2022-06-27 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='about',
            field=models.TextField(default='write about yourself here', max_length=1000, verbose_name='About'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='datetoday',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='Phone Number'),
        ),
    ]
