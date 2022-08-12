# Generated by Django 4.0.5 on 2022-07-03 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0003_rename_gold_bots_fx_bot_rename_indices_bots_gold_bot_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gold_bot',
            name='level_of_risk',
            field=models.CharField(choices=[('Super High Risk', 'Super High Risk'), ('Very Risk', 'Very Risk'), ('High Risk', 'High Risk'), ('High', 'High'), ('Moderate Risk', 'Moderate Risk'), ('Low Risk', 'Low Risk')], max_length=150, verbose_name='Risk Level'),
        ),
    ]