# Generated by Django 3.1.3 on 2020-11-09 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0006_auto_20201109_1900'),
        ('user', '0004_auto_20201108_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follow',
            field=models.ManyToManyField(through='user.FollowList', to='user.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='like',
            field=models.ManyToManyField(related_name='like_user', to='posting.Post'),
        ),
    ]
