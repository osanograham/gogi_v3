# Generated by Django 4.0.5 on 2022-07-03 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0002_fx_bots_gold_bots_indices_bots_delete_go_bots'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='gold_bots',
            new_name='fx_bot',
        ),
        migrations.RenameModel(
            old_name='indices_bots',
            new_name='gold_bot',
        ),
        migrations.RenameModel(
            old_name='fx_bots',
            new_name='indices_bot',
        ),
    ]
