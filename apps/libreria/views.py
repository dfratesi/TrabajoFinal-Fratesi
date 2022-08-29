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


class BookDetailView(LoginRequiredMixin, DetailView):
    """Vista para ver los detalles de una isntancia de
    la clase Book"""

    model = Book
    context_object_name = "libro"


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


class AuthorListView(LoginRequiredMixin, ListView):
    """Vista para ver la lista de autores"""
    model = Author
    context_object_name = "autores"

def lista_autores(request):
    autores = Author.objects.all()
    context = {"autores": autores}
    return render(request, "libreria/autor_list.html", context=context)


def autor_create(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AuthorForm()
    context = {"form": form}
    return render(request, "libreria/autor_create.html", context=context)


def autor_detail(request, pk):
    """Detalle del Autor"""
    autor = get_object_or_404(Author, pk=pk)
    return render(request, "libreria/autor_detail.html", {"autor": autor})


def lista_generos(request):
    generos = Genre.objects.all()
    context = {"generos": generos}
    return render(request, "libreria/genero_list.html", context=context)


def genero_create(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = GenreForm()
    context = {"form": form}
    return render(request, "libreria/genero_create.html", context=context)


def genero_detail(request, pk):
    """Detalle del Autor"""
    genero = get_object_or_404(Genre, pk=pk)
    return render(request, "libreria/genero_detail.html", {"genero": genero})


def search_books(request):
    search = request.GET["search"]
    libros = Book.objects.filter(
        Q(title__icontains=search)
        #| Q(author__last_name__icontains=search)
        #| Q(genre__genre__icontains=search)
    )
    context = {"libros": libros}
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
