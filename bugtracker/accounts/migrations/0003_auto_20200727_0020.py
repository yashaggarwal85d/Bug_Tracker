# Generated by Django 3.0.8 on 2020-07-27 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200727_0019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='tags',
            new_name='skills',
        ),
    ]