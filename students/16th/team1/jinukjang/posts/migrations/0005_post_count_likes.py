# Generated by Django 2.2.5 on 2021-01-01 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='count_likes',
            field=models.IntegerField(default=0),
        ),
    ]
