# Generated by Django 3.0.8 on 2020-08-08 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200808_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='online',
            field=models.BooleanField(default=False),
        ),
    ]
