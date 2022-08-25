# Generated by Django 4.1 on 2022-08-20 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("libreria", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="author",
            options={
                "ordering": ["last_name", "first_name"],
                "verbose_name": "Autor",
                "verbose_name_plural": "Autores",
            },
        ),
        migrations.AlterModelOptions(
            name="book",
            options={
                "ordering": ["title", "editorial"],
                "verbose_name": "Libro",
                "verbose_name_plural": "Libros",
            },
        ),
        migrations.AlterModelOptions(
            name="genre",
            options={"verbose_name": "Género", "verbose_name_plural": "Géneros"},
        ),
        migrations.AlterModelOptions(
            name="language",
            options={"verbose_name": "Idioma", "verbose_name_plural": "Idiomas"},
        ),
        migrations.AlterField(
            model_name="book",
            name="genre",
            field=models.ManyToManyField(
                blank=True, null=True, to="libreria.genre", verbose_name="Género"
            ),
        ),
    ]