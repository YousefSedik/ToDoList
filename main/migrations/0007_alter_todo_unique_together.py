# Generated by Django 5.0.2 on 2024-02-10 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_todo_todonote_alter_todo_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='todo',
            unique_together=set(),
        ),
    ]
