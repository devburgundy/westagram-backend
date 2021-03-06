# Generated by Django 3.1.3 on 2020-11-10 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=30)),
                ('user_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
