# Generated by Django 3.1.2 on 2020-11-10 13:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0004_auto_20201109_1336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='data',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.URLField(max_length=1000),
        ),
        migrations.AlterModelTable(
            name='comment',
            table='comments',
        ),
        migrations.AlterModelTable(
            name='post',
            table='posts',
        ),
    ]