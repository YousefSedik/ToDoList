# Generated by Django 4.2.7 on 2023-11-19 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_todo_is_done'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['is_done', 'Create_Date', 'Create_Time']},
        ),
        migrations.AlterField(
            model_name='todo',
            name='ToDoNote',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
