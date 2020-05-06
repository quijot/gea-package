# gea

Gestión de Expedientes de Agrimensores.

__gea__ es una aplicación web basada en [Django](https://www.djangoproject.com/) para gestionar expedientes de agrimensores. Hasta ahora sólo fue usada en la provincia de _Santa Fe, Argentina_.

## Requisitos previos

- GNU/Linux
- Python >= 3.6
- [Django](https://pypi.python.org/pypi/Django/) 3.0.6
- [psycopg2](https://pypi.python.org/pypi/psycopg2/) (opcional si utiliza PostgreSQL)
- [django-nested-admin](https://pypi.python.org/pypi/django-nested-admin/) (para formularios anidados)

## Instalación

```bash
$ pip install gea
```

Se instalan también los ```requirements``` como Django y nested-admin. Si además quiere utilizar PostgreSQL para la Base de Datos, deberá instalar manualmente psycopg2.

```bash
$ pip install psycopg2
```

## Puesta en marcha

### Crear proyecto Django

```bash
$ django-admin startproject estudio
```

### Editar ```settings.py``` del proyecto Django:

```bash
$ # dentro de "estudio"
$ vim estudio/settings.py
```

- Agregar __```gea```__ y ```nested_admin``` a las ```INSTALLED_APPS```:

```python
INSTALLED_APPS = (
    ...
    'gea.apps.GeaConfig',
    'nested_admin',
)
```

- Se pueden acomodar el Idioma y la TimeZone

```python
LANGUAGE_CODE = 'es-AR'
TIME_ZONE = 'America/Argentina/Buenos_Aires'
```

#### Para utilizar PostgreSQL (opcional)

- Opcionalmente, configurar la Base de Datos para utilizar PostgreSQL, de otro modo, Django usa SQLite3 por defecto. Editar ```settings.py```.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gea',
        'USER': '<postgresql-user>',
        'PASSWORD': '<postgresql-password>', # be creative
        'HOST': 'localhost',
    }
}
```

con esta opción se debe crear la BD, con el comando ```createdb``` de PostgreSQL

```bash
$ createdb gea
```

### Editar ```urls.py``` del proyecto Django:

```bash
$ # dentro de "estudio"
$ vim estudio/urls.py
```

- Importar las vistas de ```gea``` y agregar las urls de las aplicaciones que instalamos:

```python
from django.conf.urls import include, path


urlpatterns = [
    ...
    path('gea/', include('gea.urls')),
    path('_nested_admin/', include('nested_admin.urls')),
]
```

### Base de datos y Superusuario

```bash
$ # dentro de "estudio"
$ python manage.py makemigrations gea
$ python manage.py migrate
$ python manage.py createsuperuser
```

```makemigrations``` y ```migrate``` ponen a punto la base de datos, ```createsuperuser``` instala el sistema de autenticación de Django, _Django's auth system_, con lo cual, pedirá usuario, mail y contraseña, por ejemplo: _admin_ y _Af7Dr2ujW_. Con estos datos ingresaremos después a la interfaz de administración.

## Archivos estáticos (css, img, js)

Por último, algo muy importante: los archivos de estilo, imágenes y scripts que usará nuestra nueva aplicación.

Editar ```settings.py``` agregando la siguiente linea:

```python
STATIC_ROOT = './static/'
```

Y ejecutar:
```bash
$ # dentro de "estudio"
$ python manage.py collectstatic
```

¡**LISTO**... Ahora podemos probar cómo quedó nuestra django-app!

```bash
$ # dentro de "estudio"
$ python manage.py runserver
```

e ingresamos a [http://127.0.0.1:8000/gea/](http://127.0.0.1:8000/gea/)... con los datos del superusuario que creamos antes.

## LICENCIA

[MIT](LICENSE)
