# Generated by Django 4.2.7 on 2023-11-24 22:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_alter_todo_options_alter_todo_todonote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='ToDoNote',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='todo',
            unique_together={('user', 'ToDoNote')},
        ),
    ]
