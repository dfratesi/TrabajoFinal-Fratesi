from django.db import models


class Book(models.Model):
    title = models.CharField("Título", max_length=50)
    editorial = models.CharField("Editorial", max_length=50, null=True, blank=True)
    isbn = models.CharField("ISBN", max_length=13, null=True, blank=True)
    price = models.FloatField("Precio")
    language = models.ForeignKey(
        "Language", on_delete=models.SET_NULL, null=True, blank=True
    )
    genre = models.ManyToManyField("Genre", verbose_name="Género")
    author = models.ForeignKey(
        "Author",
        verbose_name="Autor",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    resumen = models.TextField("Reseña", max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title", "editorial"]


class Author(models.Model):
    first_name = models.CharField("Nombre", max_length=20, null=True, blank=True)
    last_name = models.CharField("Apellido", max_length=50)
    country = models.CharField(
        "Nacionalidad", max_length=50, null=True, blank=True, help_text="País de origen"
    )

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name_plural = "Autores"

    def fullname(self):
        return f"{self.last_name} {self.first_name}"

    def __str__(self):
        return self.fullname()


class Genre(models.Model):
    genre = models.CharField(
        "Género",
        max_length=100,
        help_text="Ingresa un género de libro (ej. Ciencia Ficción, Misterio)",
    )

    def __str__(self):
        return self.genre


class Language(models.Model):
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.language
