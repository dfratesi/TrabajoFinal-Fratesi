from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    BookCrudListView,
    AuthorListView,
    AuthorCreateView,
    AuthorUpdateView,
    AuthorDeleteView,
    AuthorCrudListView,
    author_detail,
    GenreCreateView,
    genero_detail,
    GenreUpdateView,
    GenreDeleteView,
    GenreCrudListView,
    search_books,
    idioma_create,
)

app_name = "libreria"

urlpatterns = [
    # URLs libros
    path("", BookListView.as_view(), name="book-list"),
    path("create/", BookCreateView.as_view(), name="create"),
    path("<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("<int:pk>/edit/", BookUpdateView.as_view(), name="book-update"),
    path("<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete"),
    path("crud/", BookCrudListView.as_view(), name="book-crud"),
    path("search/", search_books, name="search-book"),
    # URLs autores
    path("author/", AuthorListView.as_view(), name="author-list"),
    path("author/create/", AuthorCreateView.as_view(), name="author-create"),
    path("author/<int:pk>/", author_detail, name="author-detail"),
    path("author/<int:pk>/edit/", AuthorUpdateView.as_view(), name="author-update"),
    path("author/<int:pk>/delete/", AuthorDeleteView.as_view(), name="author-delete"),
    path("author/crud/", AuthorCrudListView.as_view(), name="author-crud"),
    # URLs generos
    path("genre/create/", GenreCreateView.as_view(), name="genre-create"),
    path("genre/<int:pk>/", genero_detail, name="genre-detail"),
    path("genre/<int:pk>/edit/", GenreUpdateView.as_view(), name="genre-update"),
    path("genre/<int:pk>/delete/", GenreDeleteView.as_view(), name="genre-delete"),
    path("genre/crud/", GenreCrudListView.as_view(), name="genre-crud"),
    # URLs idiomas
    path("idiomas/create/", idioma_create, name="idiomas-create"),
]
