# Generated by Django 3.1.3 on 2020-12-06 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201206_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='user_id',
        ),
    ]
