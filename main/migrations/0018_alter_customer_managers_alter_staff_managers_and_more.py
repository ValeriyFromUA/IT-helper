# Generated by Django 4.2 on 2023-05-09 21:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0017_customer_username"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="customer",
            managers=[],
        ),
        migrations.AlterModelManagers(
            name="staff",
            managers=[],
        ),
        migrations.RemoveField(
            model_name="customer",
            name="username",
        ),
    ]
