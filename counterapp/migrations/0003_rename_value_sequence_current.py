# Generated by Django 3.2.6 on 2021-08-07 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counterapp', '0002_sequence_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sequence',
            old_name='value',
            new_name='current',
        ),
    ]
