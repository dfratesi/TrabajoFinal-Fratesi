# Trabajo Final

![GitHub language count](https://img.shields.io/github/languages/count/dfratesi/trabajo_final?style=plastic)
![GitHub top language](https://img.shields.io/github/languages/top/dfratesi/trabajo_final?style=plastic)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=plastic&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=plastic&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=plastic&logo=sqlite&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=plastic&logo=visual-studio-code&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=plastic&logo=github&logoColor=white)

## Equipo

@dfratesi Damián Fratesi :man_shrugging:

## Instalación en Linux

1. Crear entorno

    ```python
    python3 -m venv env
    ```

2. Activar entorno

    ```pyton
    source env/bin/activate
    ```

3. Actualizar pip e instalar Django

    ```python
    pip install --upgrade pip

    pip install -r requirements.txt
    ```

4. Cargar fixtures en la base de datos

    ```python
    ./manage.py loaddata libreria.json
    ```

5. Crear superusuario

    ```python
    ./manage.py createsuperuser
    ```

6. Ejecutar el servidor

    ```python
    ./manage.py runserver
    ```

## Demo

[mucho38.pythonanywhere.com](http://mucho38.pythonanywhere.com/)

## Formulario de busqueda

El formulario esta incluido en la nabvar. Hace la busqueda por el título del libro.

## URLs

| URL | Descripción | Permisos necesarios |
| --- | --- | --- |
| / | Home del sitio | |
| admin/ | Sitio admin | Superusuario |
| books/ | Listado de los libros | |
| books/create/ | Formulario para cargar libros | Superusuario |
| books/_int_/ | Ver detalle de un libro. Se reemplaza _int_ con el _id_ del libro. | Estar logueado |
| books/crud/ | Alta, baja y modificacion de un libro | Staff |
| books/author/ | Listado de los autores | |
| books/author/create/ | Formulario para cargar un autor | Superusuario |
| books/author/_int_/ | Ver detalle de un autor. Se reemplaza _int_ con el _id_ del autor. | |
| books/author/crud/ | Alta, baja y modificacion de un autor | Staff |
| books/genre/create/ | Formulario para ingresar géneros literarios | Superusuario |
| books/genre/_int_/ | Muestra los libros de un género en particular. Se reemplaza _int_ con el _id_ del género. | |
| books/genre/crud/ | Alta, baja y modificacion de un autor | Staff |
