# Generated by Django 3.1.5 on 2021-01-05 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0003_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_num',
            field=models.IntegerField(default=0),
        ),
    ]