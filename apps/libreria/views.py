from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Book, Author, Genre
from .forms import BookForm, AuthorForm, GenreForm, LanguageForm
from django.db.models import Q
from django.views.generic import TemplateView


def home(request):
    libros = Book.objects.all().order_by("-id")[:3]
    context = {"libros": libros}
    return render(request, "index.html", context=context)


class BookListView(ListView):
    model = Book
    context_object_name = "libros"
    template_name = "libreria/libro_list.html"


# def lista_libros(request):
#    libros = Book.objects.all()
#    context = {"libros": libros}
#    return render(request, "libreria/libro_list.html", context=context)


def libro_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = BookForm()
    context = {"form": form}
    return render(request, "libreria/libro_create.html", context=context)


# def book_detail(request, pk):
#    """Detalle del libro"""
#    libro = get_object_or_404(Book, pk=pk)
#    return render(request, "libreria/libro_detail.html", {"libro": libro})


class BookDetailView(DetailView):
    model = Book
    context_object_name = "libro"
    template_name = "libreria/libro_detail.html"


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
        | Q(autor__last_name__icontains=search)
        | Q(genero__name__icontains=search)
    )
    context = {"libros": libros}
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
