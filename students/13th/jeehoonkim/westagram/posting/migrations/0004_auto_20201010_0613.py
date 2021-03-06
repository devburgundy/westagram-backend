# Generated by Django 3.1.1 on 2020-10-10 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('posting', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='like',
            field=models.ManyToManyField(related_name='like_posting', to='user.User'),
        ),
        migrations.AlterField(
            model_name='posting',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_posting', to='user.user'),
        ),
    ]
