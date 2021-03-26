# Curso de Django

## 1. Introducción a Django


## 2. Preparación del entorno de trabajo

* Instalar pip3
* Instalar python
* Crear un entorno virtual con 'python3 -m -venv .env' . Se genera un entorno en una carpeta oculta.
* Activamos el entorno virtual ejecutando 'source .env/bin/activate'

## 3. Crear un nuevo proyecto

Con el entorno virtual activado, iniciamos el comando de administración de django:
``` django-admin```
Nos aparecerán las siguientes opciones:
```
Available subcommands:
[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject    (crear un nuevo proyecto)
    test
    testserver

```
Creamos un nuevo proyecto dentro de la propia carpeta que hemos creado (createproject nombredelproyecto rutadelacarpeta)
```django-admin createproject platzigram . ```

Entonces, se generan los siguientes archivos automaticamente:

./manage.py --> Interfaz sobre django-admin
./platzigram/__init__.py  --> Script que declara la carpeta como un módulo de python.
./platzigram/asgi.py      --> ??
./platzigram/settings.py  --> Script que incluye las configuraciones del servidor.
./platzigram/urls.py      --> Script principal que gestiona las URL. Es el punto de entrada para todas las peticiones al servidor.
./platzigram/wsgi.py      --> Interfaz de django para hacer deploy a producción.


### settings.py
BASE_DIR --> Ruta que declara la ubicación donde corre el proyecto.
SECRET_KEY --> Hashing de las contraseñas y sesiones.
DEBUG --> True si estamos en desarollo, False si estamos en producción.
ALLOWED_HOSTR --> Hosts permitidos para interactuar con el proyecto.
INSTALLED_APPS --> Aplicaciones ligadas al proyecto.
MIDDLEWARE --> 
ROOT_URLCONF --> Ruta al archivo de URLs principal.
TEMPLATES --> Config de plantillas.
WSGI_APPLICATION --> Ruta al archivo wsgi.py.
DATABASES --> configuración de consultas a BBDD (por defecto SQLITE3).
AUTH_PASSWORD_VALIDATORS --> Validadores de contraseña para el uso de sesiones.
LANGUAGE_CODE --> Idioma de interacción
TIME_ZONE --> Zona horaria
USE_I18N --> Traducción
USE L10N --> Traducción
USE_TZ --> Timezone
STATIC_URL --> Indica la ruta que se le da a los archivos estáticos para que carguen automaticamente si son solicitados, sin pasar por URLs.

### Iniciamos el servidor con manage.py
Ejecutamos ```python3 manage.py```
Se abre la interfaz similar a django-admin pero con mas opciones.
Iniciamos el servidor con ```python3 manage.py runserver```

Para acceder al servidor: http://localhost:8000/

### Hola mundo
Creamos el path para la url hello-world que genere una vista (una función) al ser requerida.
```path ('url',funcion)```

## 4. Request

Django procesa las requests o peticiones siguiendo el siguiente esquema:

1. Recive una petición http desde el cliente.
2. Busca la ruta del archivo de URLs en la variable ROOT_URLCONF del archivo settings.py.
3. Busca la variable urlpatterns en el archivo de URLs.
4. Busca dentro de urlpatterns la URL que coincida con la solicitada.
5. Ejecuta la vista/función que corresponda a la URL pasandole los siguientes argumentos:
* Instancia de un objeto HttpRequest
* Argumentos que contiene la propia URL (opcional)
* Argumentos adicionales que podamos incluir
6. Si no encuentra ninguna URL, lanza una excepcion.

## views.py
Creamos un archivo views.py que alojará las vistas/funciones.


## 5. Response

### httpResponse
```
from django.http import HttpResponse

def httpresponse(request):
    return HttpResponse('value')
  ```
  
### JsonResponse
```
from django.http import JsonResponse

def jsonresponse(request):
    return JsonResponse({'key':value})
  ```
