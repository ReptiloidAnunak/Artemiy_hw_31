# Generated by Django 4.2.2 on 2023-06-25 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0009_rename_owner_selection_author"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ad",
            old_name="author",
            new_name="owner",
        ),
    ]