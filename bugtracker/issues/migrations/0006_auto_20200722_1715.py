# Generated by Django 3.0.8 on 2020-07-22 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0005_issue_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='slug',
            field=models.SlugField(allow_unicode=True, unique=True),
        ),
    ]
