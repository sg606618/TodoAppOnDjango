# Generated by Django 5.0.6 on 2024-06-26 22:24

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_blog_todo_alter_todo_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='name',
        ),
        migrations.AddField(
            model_name='todo',
            name='title',
            field=models.CharField(default=datetime.datetime(2024, 6, 26, 22, 24, 55, 678804), max_length=50, validators=[django.core.validators.MinLengthValidator(5)]),
            preserve_default=False,
        ),
    ]
