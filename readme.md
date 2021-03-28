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

## Argumentos a través de la URL

Los path converters permiten incluir variables en las URL que Django se encarga de procesar como argumentos de las vistas. Estos se describen enla variable 'urlpatterns' del script 'urls.py' con el siguiente formato:

```
urlpatterns = [
  path('hi/<str:name>/<int:age>',views.check_age)
]
```
Esta vista se procesa en el script 'views.py' donde se ejecuta la fución que recibe los argumentos de la url:
```
def check_age(request,name,age):

    if age < 18:
        message = 'Lo sentimos, tienes que ser mayor de edad para usar este servicio.'
    else:
        message = 'Bienvenido a nuestro servicio'
    return HttpResponse(f'Hola, {name}. Tu edad es de {age} años. {message}')
```

Por ejemplo, con la url 'http://localhost:8000/hi/sergio/17' la respuesta sería:
'Hola, sergio. Tu edad es de 17 años. Lo sentimos, tienes que ser mayor de edad para usar este servicio.'


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

dictionary = {
  'key':value
}

def jsonresponse(request):
    return JsonResponse(dicctionary)
  ```



## 6.Apps

Para crear una aplicación de Django, usamos el comando 'createapp' de manage.py dandole como atributo el nombre de la app.
```python3 manage.py createapp nombredelaapp```
Se crean automaticamente un conjunto de scripts para la app:
* migrations
* admin.py
* models.py
* tests.py
* views.py

## 7. Template
Los templates son los scripts que se encargan de presentar los datos de la lógica en un archivo html de una forma más eficiente. Las rutas a las templates se encuentran en la variable TEMPLATES de settings.py. Si la llave APP_DIR = True, permite que django encuentre automaticamente los archivos html que estén dentro de los directorios "templates" de las diferentes apps, de modo que no es necesario indicar la ruta al hacer el render.

Para crear un nuevo template, creamos una carpeta dentro de la carpeta de la app correspondiente con el nombre "templates", en la que iremos generando los diferentes archivos html correspondientes.

Para mostrar la pagina html en el navegador se usa la función render de django.shorcuts. Esta se genera normalmente en el return de la vista con los argumentos de la request, el nombre del archivo html y el contexto (que es un diccionario que agrupa las variables resultantes de la lógica y que tengan que mostrarse).
```
from django.shorcuts import render

def show_page(request):
  
  context={
    'key':value
    }
  
  return render(request,'page.html',context)
```
Dentro del template, en HTML, las variables del contexto se muestran con la siguiente notación: 
```
{{ key }}
```
También se pueden incluir lógicas de programación en los templates con la notación (ver documentacion de Template System - Build In de Django):
```
{%for post in posts%}
  {{post}}
{%endfor%}
```
Para este proyecto se usa Bootstrap como hoja de estilos (ver feed.html)