# Generated by Django 5.1 on 2024-10-01 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_datecompleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, max_length=150),
        ),
    ]
