# Generated by Django 4.1.7 on 2024-02-05 00:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("{{ cookiecutter.app_name }}", "0002_create_{{cookiecutter.model_singular_lower}}"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ActivityLog",
        ),
    ]