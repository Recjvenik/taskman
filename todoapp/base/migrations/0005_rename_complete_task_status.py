# Generated by Django 4.0.3 on 2022-03-29 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_task_complete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='complete',
            new_name='status',
        ),
    ]
