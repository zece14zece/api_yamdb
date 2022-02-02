# Generated by Django 2.2.16 on 2022-02-02 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.TextField(choices=[('user', 'Пользователь'), ('moderator', 'Модератор'), ('admin', 'Админ')], default=('user', 'Пользователь'), verbose_name='Роль'),
        ),
    ]
