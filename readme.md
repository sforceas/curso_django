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

## 8. Patrones de diseño y Django
Un patrón de diseño, en términos generales, es una solución reutilizable a un problema común.
El patrón más común para el desarrollo web es MVC (Model, View, Controller). Django implementa un patrón similar llamado MTV (Model, Template, View).

### Model
Es la forma en la que creamos esquemas de objetos (un usuario, un post, etc) para representarlos en nuestra base de datos.
El modelo sin importar nuestro sistema ge BD (mysql, postgress, etc) nos ayudara a crear esta entidad a través de un OMR, esto nos ahorra la molestia de tener que escribir las sentencias de SQL para crear las tablas y atributos.

El Modelo en Django usa diferentes opciones para conectarse a múltiples bases de datos relacionales, entre las que se encuentran: SQLite, PostgreSQL, Oracle y MySQL. 
Para la creación de tablas, Django usa la técnica del ORM (Object Relational Mapper), una abstracción del manejo de datos usando OOP.

https://docs.djangoproject.com/en/2.0/ref/settings/#databases
https://docs.djangoproject.com/en/2.0/ref/models/fields/

La configuración de las bases de datos se realiza en el scritp "settings.py", en la variable DATABASES. Por defecto, django crea una base dedatos de SQLITE que solo necesita de un archivo que contiene todas las tablas.

Al añadir apps de Django, tenemos una advertencia en la consola que nos indica que migremos los cambios a la base de datos. Esto permite actualizar las tablas con el comando ```python3 manage.py migrate``` de forma automatica.

Si creamos un nuevo modelos, los podemos refleja estos cambios mediante ```python3 platzigram/manage.py makemigrations``` y, luego, reflejar esos cambios medinte ```python3 manage.py migrate```.

Estas nuevas tablas van a reflejarse en la base de datos identificandose como: app_modelo, por ejemplo: posts_users.


### Template
Es el encargado de manejar la lógica y sintaxis de la información que se va a presentar en el cliente, el sistema de templates de django usa HTML para ello.

### View
Su función es solo suministrar datos al template
 
Manda la información necesaria el template para que este pueda manejar los datos y presentarlos de una manera correcta.


## 9. ORM de Django

ORM: Object-relational mapping. Es el encargado de permitir
el acceso y control de una base de datos relacional a través de
una abstracción a clases y objetos.

## Escribir datos en BDD
Para comprender el ORM de django, inciciamos un shell de python desde Django. Para ello, ejecutamos la función "shell" en manage.py con el comando:  ```python3 manage.py shell```. Se abrirá un shell de python desde el que podemos ejecutar diferentes comandos. En este caso cargaremos datos en la base de datos, concretamente en la tabla post_user que hemos definido en la clase User en posts/models.py.

Para ello, primero importamos la clase User desde el módulo posts.models. También importamos 'date' para dar formato de fecha a un string. 
```
from datetime import date
from posts.models import User
```
Posteriormente, cargamos una lista de usuarios con los datos completados. Cada usuario se estructura como un diccionario, en el que la llave corresponde con un campo del modelo y de la BDD. En este ejemplo se incluye un ejemplo de elemento:

```
users = [
  {
        'email': 'arturo@mail.com',
        'first_name': 'Arturo',
        'last_name': 'Martínez',
        'password': '123456',
        'is_admin': True,
        'birthdate': date(1981, 11, 6),
        'bio': "Bografia de mi vida!"
    }
]
```
Finalmente realizamos la operacion de escritura en la base de datos mediante un loop for que recorre cada diccionario incluido en la lista de usuarios, crea una instancia/objeto de esa clase con los datos del diccionario (**user) y los guarda con .save(). Finalmente imprime el mail y el id para comprobar que se ha escrito correctamente.
```
for user in users:
  obj = User(**user)
  obj.save()
  print(obj.pk, ':', obj.email)
```

## Lectura en la BDD
Para traer un unico objeto de una base de datos usamos el método class.objects.get(key = 'value') Para ello tenemos que haber importado la clase User de models.py. El resultado de la query es una instancia de la clase User (por lo tanto es un objeto), de modo que podemos acceder a los datos de este objeto mediante la sintaxis objeto.llave
```
from posts.models import User

user = User.objects.get(email='freddier@platzi.com'
print(user.email)
```
Si queremos realizar un filtro de datos usaremos el método class.objects.filter(key='value'). En este caso haremos una query especial usando dos guiones bajos para filtrar según como terminan los emails.
```
from posts.models import User

platzi_users = User.objects.filter(email__endswith='@platzi.com'
print(platzi_users.email)
```

Si quisieramos traer todos los objetos usariamos class.objects.all()
```
all_users = User.objects.all()
```


### Modificando la representacion de las querys
Por defecto cuando hacemos una lectura de la base de datos nos devuelve el id del objeto. Si queremos que nos devuelva por defecto otro valor identificativo, como el mail, crearemos una función dentro de la clase correspondiente en models.py.

```
def __str__(self):
  # Return email
  return self.email
```
### Actualizando la BDD
Si queremos aplicar un filtro y actualizar los valores de los objetos que cumplen este filtro, usamos Class.objects.filter(value1='value1').update(value2='value2'). En este ejemplo queremos que los que tengan mail @platzi.com sean todos is_admin=True. Este método update devuelve un numero entero que cuenta el número de objetos actualizados.
```
update_users = User.objects.filter(email__endswith='@platzi.com').update(is_admin=True)
```

Making queries | Django documentation | Django
https://docs.djangoproject.com/en/2.0/topics/db/queries/


## 10. Aplicacion Django Auth
Las opciones que Django propone para implementar Usuarios personalizados son:
- Usando el Modelo proxy
- Extendiendo la clase abstracta de Usuario existente

Para el presente proyecto debemos crear los campos de usuario:

website
biography
phone_number
profile picture
created
modified
Luego debemos crear la app que se llamará users
```
python3 manage.py startapp users
```
Crear el modelo
Se debe importar lo que necesitamos
```
from django.contrib.auth.models import User
```
Luego se crea los campos adicionales que se necesitan según el proyecto
```
class Profle (models.Model):
    """Profile Model."""
    """Proxy model that extends the base data with other information"""
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    website=models.URLField(max_length=200,blank=True)
    biography=models.TextField(blank=True)
    phone_number=models.CharField(max_length=20,blank=True)
    picture=models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )
    create=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)


    def __str__(self):
        """Return username."""
        return self.user.username
```
Posterior a eso dirigirse al archivo de settings.py y así como se instaló post se va a instalar users

Para que funcione el campo ImageField se debe instalar la librería Pillow y se lo hace de la siguiente manera
```
pip install Pillow
```
Después ejecutar para que se hagan efecto las migraciones
```
python3 manage.py makemigrations
python3 manage.py migrate
```
Y para ingresar al administrador de django crear el super usuario
```
python3 manage.py createsuperuser
```
Para acceder al panel de administración de Django, por defecto se accede mediante localhost:8000/admin y iniciando sesión con un superuser.

Registraremos el perfil que acabamos de customizar, junto con el modelo extendido de Usuario, en el users.admin.py de Django para poder manejarlo desde la aplicación.
Esto puede hacerse de dos formas: con admin.site.register(Profile) o creando una nueva clase que herede de Admin.ModelAdmin.
https://docs.djangoproject.com/en/2.2/ref/contrib/admin/


## 11. Templates y static
html y css

## 12. Login y Logout de Django
Ver documentacion
https://docs.djangoproject.com/en/2.0/topics/auth/default/#how-to-log-a-user-out



### Logout
En el archivo views.py de la app users introducimos la siguiente función:
```
@login_required
def logout_view(request):
  logout(request)
  # Redirect to a success page
  return redirect('feed')  
```
Para poder hacer logout necesitamos que previamente hayamos hecho login, por eso el decorador @login_required.

Para hacer llamar esta función deberemos registrar la el path en el archivo urls.py.     
```
path('users/logout/',users_views.logout_view,name='logout')
```
Para incluir un botón de navegación con la función logout, añadimos el siguiente codigo en la barra de navegación nav.html. El formato {%url "nombre_del_path"%} usa los atributos name que se le dan a los paths en el archivo urls.py.

```
<a href="{% url "logout"%}">
  <i class="fas fa-sign-out-alt"></i>
</a>
```

### Creacion de usuarios (Sign Up)
https://docs.djangoproject.com/en/2.0/topics/auth/default/#creating-users
En este caso queremos crear un usuario a partir de nuestro modelso Profile, que extiende el de User (de django.contrib.auth).

En el archivo views.py de la app users introducimos la siguiente función:
```
def signup_view(request):
    '''Signup view'''

    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST.get('password', True)
        password_confirm = request.POST.get('password_confirm', True)

        
        # PASSWORD VALIDATION
        if password != password_confirm:
            error = 'The passwords do not match.'
            return render(request, 'users/signup.html', {'error': error})
        
        # EMAIL VALIDATION
        u = User.objects.filter(email=email)
        if u:
            error = f'There is another account using {email}'
            return render(request, 'users/signup.html', {'error': error})
        
        # USERNAME VALIDATION 
        try:
            user = User.objects.create_user(username=username, password=password)
            user.email = email
            user.save()

            profile = Profile(user=user)
            profile.save()

            login(request, user)
            return redirect('feed') # CAMBIAR >> Redireccionar a completar perfil
        except IntegrityError as ie:
            error = f'There is another account using {usermame}'
            return render(request, 'users/signup.html', {'error': error})

    return render(request, 'users/signup.html')
```

Para hacer llamar esta función deberemos registrar la el path en el archivo urls.py.     
```
path('users/signup/',users_views.signup_view,name='signup')
```
Para incluir un botón de navegación con la función logout, añadimos el siguiente codigo en la barra de navegación nav.html. El formato {%url "nombre_del_path"%} usa los atributos name que se le dan a los paths en el archivo urls.py.

```
<a href="{% url "signup"%}">
  <i class="fas fa-sign-out-alt"></i>
</a>
```




## 13. Middlewares
Un middleware en Django es una serie de hooks y una API de bajo nivel que nos permiten modificar el objeto request antes de que llegue a la vista y response antes de que salga de la vista.

https://docs.djangoproject.com/en/2.0/topics/http/middleware/

Django dispone de los siguientes middlewares por defecto:

* SecurityMiddleware
* SessionMiddleware
* CommonMiddleware
* CsrfViewMiddleware
* AuthenticationMiddleware (nos permite acceder a datos del usuario directamente desde cualquier template mediante {{request.user.username}}, por ejemplo).
* MessageMiddleware
* XFrameOptionsMiddleware

Crearemos un middleware para redireccionar al usuario al perfil para que actualice su información cuando no haya definido aún biografía o avatar.

![](https://cdn-images-1.medium.com/max/800/1*t9TAX89Y3rZUXth2Le07Xg.png)

Pasos a seguir:
1. Crear un path en urls.py llamado update_profile
```
path('users/me/profile/',users_views.update_profile,name='update_profile')

```
3. Crear una función update_profile en users.models
4. Crear un render html de la pagina de update
5. Crear un archivo middleware.py en la app principal. En él crearemos una clase para el middleware que incluya una función __ call __ que es la que ejecutará el la logica.
7. Asignar el middleware en settings.py
```
MIDDLEWARE = [
...
'platzigram.middleware.ProfileCompletionMiddleware',
]
```


## 14. Formularios
La clase utilitaria para formularios de Django nos ayuda a resolver mucho del trabajo que se realiza de forma repetitiva. La forma de implementarla es muy similar a la implementación de la clase models.model.

Algunas de las clases disponibles en Django al implementar form, son:

* BooleanField
* CharField
* ChoiceField
* TypedChoiceField
* DateField
* DateTimeField
* DecimalField
* EmailField
* FileField
* ImageField

https://docs.djangoproject.com/en/2.0/topics/forms/
https://docs.djangoproject.com/en/2.0/ref/forms/fields/
