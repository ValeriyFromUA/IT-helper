# Generated by Django 4.2 on 2023-04-28 04:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0010_category_task_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="category",
        ),
        migrations.DeleteModel(
            name="Category",
        ),
    ]
