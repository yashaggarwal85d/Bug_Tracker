# Generated by Django 3.0.8 on 2020-07-22 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0009_remove_issue_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='issuemember',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='issuemember',
            name='issue',
        ),
        migrations.RemoveField(
            model_name='issuemember',
            name='user',
        ),
        migrations.DeleteModel(
            name='Issue',
        ),
        migrations.DeleteModel(
            name='IssueMember',
        ),
    ]
