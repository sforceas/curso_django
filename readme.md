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
