# Trabajo Final

![GitHub language count](https://img.shields.io/github/languages/count/dfratesi/trabajo_final?style=plastic)
![GitHub top language](https://img.shields.io/github/languages/top/dfratesi/trabajo_final?style=plastic)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=plastic&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=plastic&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=plastic&logo=sqlite&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=plastic&logo=visual-studio-code&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=plastic&logo=github&logoColor=white)

## Equipo

@github/dfratesi Damián Fratesi :man_shrugging:

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

## Formulario de busqueda

El formulario esta incluido en la nabvar.

## URLs

| URL | Descripción |
| --- | --- |
| / | Home del sitio |
| libros/ | Listado de los libros |
| libros/create/ | Formulario para cargar libros |
| libros/_int_/ | Ver detalle de un libro. Se reemplaza _int_ con el _id_ del libro. |
| libros/autores/ | Listado de los autores |
| libros/autores/create/ | Formulario para ingresar autores |
| libros/autores/_int_/ | Ver detalle de un autor. Se reemplaza _int_ con el _id_ del autor. |
| libros/generos/ | Listado de los géneros literarios |
| libros/generos/create/ | Formulario para ingresar géneros |
| libros/generos/_int_/ | Ver detalle de un género literario. Se reemplaza _int_ con el _id_ del género. |
| libros/idiomas/create/ | Formulario para ingresar idiomas |
