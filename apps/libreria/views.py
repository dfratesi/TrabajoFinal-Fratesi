from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from .models import Book, Author, Genre
from .forms import BookForm, AuthorForm, GenreForm, LanguageForm
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

User = get_user_model()


def home(request):
    libros = Book.objects.all().order_by("-id")[:3]
    context = {"libros": libros}
    return render(request, "index.html", context=context)


class BookListView(ListView):
    """Vista para ver la lista de libros"""

    model = Book
    context_object_name = "libros"
    queryset = (
        Book.objects.all()
        .prefetch_related(
            "genre",
        )
        .select_related("author")
    )


class BookDetailView(DetailView):
    """Vista para ver los detalles de una instancia de
    la clase Book"""

    model = Book
    context_object_name = "libro"


class BookCreateView(LoginRequiredMixin, CreateView):
    """Vista para agregar Libros"""

    model = Book
    form_class = BookForm
    template_name_suffix = "_create_form"
    success_url = reverse_lazy("libreria:book-crud")


class BookUpdateView(LoginRequiredMixin, UpdateView):
    """Vista para editar Libros"""

    model = Book
    form_class = BookForm
    template_name_suffix = "_edit_form"
    success_url = reverse_lazy("libreria:book-crud")


class BookDeleteView(LoginRequiredMixin, DeleteView):
    """Vista para borrar un libro"""

    model = Book
    context_object_name = "libro"
    success_url = reverse_lazy("libreria:book-crud")


class BookCrudListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = "libros"
    template_name = "libreria/book_crud.html"
    queryset = (
        Book.objects.all()
        .prefetch_related(
            "genre",
        )
        .select_related("author")
    )


class AuthorListView(ListView):
    """Vista para ver la lista de autores"""

    model = Author
    context_object_name = "autores"


def author_detail(request, pk):
    """Detalle del Autor y listado de sus libros"""
    aviso = ""
    autor = get_object_or_404(Author, pk=pk)
    libros = Book.objects.filter(author=autor)
    if libros.count() == 0:
        aviso = "No hay libros de este autor."
    context = {
        "autor": autor,
        "libros": libros,
        "aviso": aviso,
    }
    print(libros)
    return render(request, "libreria/author_detail.html", context)


class AuthorCreateView(LoginRequiredMixin, CreateView):
    """Vista para agregar Autores"""

    model = Author
    form_class = AuthorForm
    template_name_suffix = "_create_form"
    success_url = reverse_lazy("libreria:author-crud")


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    """Vista para editar Autores"""

    model = Author
    form_class = AuthorForm
    template_name_suffix = "_edit_form"
    success_url = reverse_lazy("libreria:author-crud")


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    """Vista para borrar un Autor"""

    model = Author
    context_object_name = "autor"
    success_url = reverse_lazy("libreria:author-crud")


class AuthorCrudListView(LoginRequiredMixin, ListView):
    model = Author
    context_object_name = "autores"
    template_name = "libreria/author_crud.html"


def genero_detail(request, pk):
    """Detalle del Género"""
    genero = get_object_or_404(Genre, pk=pk)
    libros = Book.objects.filter(genre=genero)
    cantidad = libros.count()
    context = {
        "genero": genero,
        "libros": libros,
        "cantidad": cantidad,
    }
    return render(request, "libreria/genre_detail.html", context)


class GenreCreateView(LoginRequiredMixin, CreateView):
    """Vista para agregar Géneros"""

    model = Genre
    form_class = GenreForm
    template_name_suffix = "_create_form"
    success_url = reverse_lazy("libreria:genre-crud")


class GenreUpdateView(LoginRequiredMixin, UpdateView):
    """Vista para editar Géneros"""

    model = Genre
    form_class = GenreForm
    template_name_suffix = "_edit_form"
    success_url = reverse_lazy("libreria:genre-crud")


class GenreDeleteView(LoginRequiredMixin, DeleteView):
    """Vista para borrar un Género"""

    model = Genre
    context_object_name = "genero"
    success_url = reverse_lazy("libreria:genre-crud")


class GenreCrudListView(LoginRequiredMixin, ListView):
    model = Genre
    context_object_name = "generos"
    template_name = "libreria/genre_crud.html"


def search_books(request):
    search = request.GET["search"]
    libros = Book.objects.filter(
        Q(title__icontains=search)
        # | Q(author__last_name__icontains=search)
        # | Q(genre__genre__icontains=search)
    )
    context = {"libros": libros, "search": search}
    print(context)
    return render(request, "libreria/book_search.html", context=context)


def idioma_create(request):
    if request.method == "POST":
        form = LanguageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = LanguageForm()
    context = {"form": form}
    return render(request, "libreria/idioma_create.html", context=context)


class AboutView(TemplateView):
    template_name = "about.html"
