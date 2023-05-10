# Generated by Django 4.2 on 2023-05-09 20:42

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0015_remove_callback_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="username",
        ),
        migrations.AddField(
            model_name="customer",
            name="name",
            field=models.CharField(default="Anonim", max_length=200),
        ),
        migrations.AlterField(
            model_name="customer",
            name="is_confirmed",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="customer",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, region=None, unique=True
            ),
        ),
    ]
