# Generated by Django 3.1.3 on 2020-11-10 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20201110_1358'),
        ('posting', '0005_auto_20201109_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='user.user'),
        ),
    ]