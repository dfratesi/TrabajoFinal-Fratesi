from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        verbose_name="Usuario",
        on_delete=models.CASCADE,
        related_name="profile",
    )
    phone = models.CharField("Telefono", max_length=20, null=True, blank=True)
    address = models.CharField("Direccion", max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="profile_image/", null=True, blank=True)
    # TODO: makemigrations and migrate

    def __str__(self):
        return f"{self.user.username} profile"

    def get_absolute_url(self):
        """
        Devuelve el URL de una instancia particular de un un perfil
        """
        return reverse("profile", args=[self.id])

    class Meta:
        ordering = ["user"]
        verbose_name_plural = "Perfiles"
        verbose_name = "Perfil"
