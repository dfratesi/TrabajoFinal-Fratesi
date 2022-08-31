from django.urls import path
from .views import (
    AuthorListView,
    autor_create,
    autor_detail,
    lista_generos,
    genero_create,
    genero_detail,
    search_books,
    idioma_create,
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    BookCrudListView,
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
    path("author/", AuthorListView.as_view(), name="autores-list"),
    path("author/create/", autor_create, name="autor-create"),
    path("author/<int:pk>/", autor_detail, name="autor-detail"),
    #path("author/crud/", autor_detail, name="autor-crud"),
    # URLs generos
    path("genres/", lista_generos, name="genre-list"),
    path("genres/create/", genero_create, name="genre-create"),
    path("genres/<int:pk>/", genero_detail, name="genre-detail"),
    # URLs idiomas
    path("idiomas/create/", idioma_create, name="idiomas-create"),
]
