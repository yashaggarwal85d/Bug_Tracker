# Generated by Django 3.0.8 on 2020-08-08 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
