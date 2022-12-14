from django.db import models
from django.urls import reverse


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
        related_name="author_books",
    )
    image = models.ImageField(
        "Tapa del libro", upload_to="books/", null=True, blank=True
    )
    resumen = models.TextField("Reseña", max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Devuelve el URL de una instancia particular de un Libro
        """
        return reverse("libreria:book-detail", args=[self.id])

    class Meta:
        ordering = ["title", "editorial"]
        verbose_name = "Libro"
        verbose_name_plural = "Libros"


class Author(models.Model):
    first_name = models.CharField("Nombre", max_length=20, null=True, blank=True)
    last_name = models.CharField("Apellido", max_length=50)
    country = models.CharField(
        "Nacionalidad", max_length=50, null=True, blank=True, help_text="País de origen"
    )

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.fullname()

    def get_absolute_url(self):
        """
        Devuelve el URL de una instancia particular de un Libro
        """
        return reverse("libreria:author-detail", args=[self.id])


class Genre(models.Model):
    genre = models.CharField(
        "Género",
        max_length=100,
        help_text="Ingresa un género de libro (ej. Ciencia Ficción, Misterio)",
    )

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
        ordering = [
            "genre",
        ]

    def __str__(self):
        return self.genre

    def get_absolute_url(self):
        """
        Devuelve el URL de una instancia particular de un Género
        """
        return reverse("libreria:genre-detail", args=[self.id])


class Language(models.Model):
    language = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Idioma"
        verbose_name_plural = "Idiomas"

    def __str__(self):
        return self.language

    def get_absolute_url(self):
        """
        Devuelve el URL de una instancia particular de un Libro
        """
        return reverse("libreria:genre-detail", args=[self.id])
