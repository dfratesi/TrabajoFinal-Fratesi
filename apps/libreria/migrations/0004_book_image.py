# Generated by Django 4.1 on 2022-08-20 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("libreria", "0003_alter_book_genre"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="books/", verbose_name="Tapa del libro"
            ),
        ),
    ]
