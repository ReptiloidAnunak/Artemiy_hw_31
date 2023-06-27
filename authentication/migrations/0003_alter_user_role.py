# Generated by Django 4.2.2 on 2023-06-20 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0002_remove_user_location_user_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("member", "Участник"),
                    ("moderator", "Модератор"),
                    ("admin", "Администратор"),
                ],
                default="member",
                max_length=10,
            ),
        ),
    ]
