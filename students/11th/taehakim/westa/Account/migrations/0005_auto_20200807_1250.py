# Generated by Django 3.0.8 on 2020-08-07 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_auto_20200807_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone_num',
            field=models.CharField(max_length=50),
        ),
    ]
