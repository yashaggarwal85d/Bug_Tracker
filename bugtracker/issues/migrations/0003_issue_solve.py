# Generated by Django 3.0.8 on 2020-07-22 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_auto_20200721_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='solve',
            field=models.BooleanField(default=False),
        ),
    ]
