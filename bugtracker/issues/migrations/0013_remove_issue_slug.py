# Generated by Django 3.0.8 on 2020-07-22 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0012_auto_20200722_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='slug',
        ),
    ]
