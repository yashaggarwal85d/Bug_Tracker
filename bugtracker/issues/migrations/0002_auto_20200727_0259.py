# Generated by Django 3.0.8 on 2020-07-27 09:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='message',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
