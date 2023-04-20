# API REST Asíncrona con FastAPI

Este proyecto es una API REST asíncrona creada con FastAPI en Python. La aplicación permite realizar operaciones CRUD (Crear, Leer, Actualizar y Borrar) en dos modelos: usuarios y artículos. Los usuarios pueden registrarse en la aplicación y obtener un token de autenticación, el cual deberán enviar en las cabeceras de las solicitudes que realicen a las rutas protegidas. Los artículos pueden ser creados, leídos, actualizados y eliminados, siempre y cuando el usuario esté autenticado.

## Instalación

Para instalar la aplicación, se recomienda utilizar Python 3.7 o superior y seguir estos pasos:

1.  Clonar el repositorio en tu máquina local.
2.  Crear un entorno virtual: `python -m venv env` o `virtualenv env` (dependiendo de la versión de Python que tengas instalada).
3.  Activar el entorno virtual: `source env/bin/activate` o `env\Scripts\activate` (dependiendo del sistema operativo).
4.  Instalar las dependencias: `pip install -r requirements.txt`.
5.  Crear una base de datos PostgreSQL y configurar la conexión en `config.py`.
6.  Ejecutar las migraciones de la base de datos: `alembic upgrade head`.
7.  Iniciar la aplicación: `uvicorn main:app --reload`.
8. También habrá que renombrar el env-template a '.env' y sustuir las variables de entorno por las adecuadas.

## Uso

Una vez iniciada la aplicación, podrás acceder a ella en `http://127.0.0.1:8000`. A continuación, se describen los endpoints disponibles:

### GET /articles

Retorna todos los artículos existentes en la base de datos.

#### Parámetros

Ninguno.

#### Respuestas

-   **200 OK**: Se retornan los artículos existentes en la base de datos.

### POST /articles

Crea un nuevo artículo en la base de datos.

#### Parámetros

-   **title**: Título del artículo.
-   **description**: Descripción del artículo.

#### Respuestas

-   **201 CREATED**: El artículo ha sido creado exitosamente.
-   **400 BAD REQUEST**: Error en los parámetros enviados.
-   **401 UNAUTHORIZED**: El usuario no está autenticado.

### GET /articles/{id}

Retorna el artículo con el ID especificado.

#### Parámetros

-   **id**: ID del artículo a buscar.

#### Respuestas

-   **200 OK**: Se retorna el artículo con el ID especificado.
-   **404 NOT FOUND**: No se encontró el artículo con el ID especificado.

### PUT /articles/{id}

Actualiza el artículo con el ID especificado.

#### Parámetros

-   **id**: ID del artículo a actualizar.
-   **title**: Nuevo título del artículo.
-   **description**: Nueva descripción del artículo.

#### Respuestas

-   **202 ACCEPTED**: El artículo ha sido actualizado exitosamente.
-   **400 BAD REQUEST**: Error en los parámetros enviados.
-   **401 UNAUTHORIZED**: El usuario no está autenticado.
-   **404 NOT FOUND**: No se encontró el artículo con el ID especificado.

### DELETE /articles/{id}

Elimina el artículo con el ID especificado.

#### Parámetros

-   **id**: ID del artículo a eliminar.

#### Respuestas

-   **204 NO CONTENT**: El artículo ha sido eliminado exitosamente.
-   **401 UNAUTHORIZED**: El usuario no está autenticado
