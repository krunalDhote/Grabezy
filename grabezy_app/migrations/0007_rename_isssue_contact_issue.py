# Generated by Django 3.2.6 on 2021-10-18 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grabezy_app', '0006_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='isssue',
            new_name='issue',
        ),
    ]
