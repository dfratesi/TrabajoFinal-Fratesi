from django import forms
from .models import Book, Author, Genre, Language


class BookForm(forms.ModelForm):
    """Form para agregar y editar Books"""

    class Meta:
        model = Book
        fields = "__all__"


class AuthorForm(forms.ModelForm):
    """Form para agregar y editar autores"""

    class Meta:
        model = Author
        fields = "__all__"


class GenreForm(forms.ModelForm):
    """Form para agregar y editar generos literarios"""

    class Meta:
        model = Genre
        fields = "__all__"


class LanguageForm(forms.ModelForm):
    """Form para agregar y editar Languages"""

    class Meta:
        model = Language
        fields = "__all__"
