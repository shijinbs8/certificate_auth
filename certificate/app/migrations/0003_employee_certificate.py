# Generated by Django 4.2.3 on 2024-04-29 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_auto_20240423_1448"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="certificate",
            field=models.ImageField(default=1, upload_to="images/"),
            preserve_default=False,
        ),
    ]