# Generated by Django 4.2.2 on 2023-06-24 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0012_alter_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
