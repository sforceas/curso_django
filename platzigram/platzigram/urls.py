"""platzigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from platzigram import views as local_views
from posts import views as posts_views
from users import views as users_views


"""
Librerias para poder visualizar imagenes o media desde el panel de administracion.
"""
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('hello-world',local_views.hello_world, name = 'hello_world'), # Al acceder a la url se ejecuta una función
    path('numbers',local_views.numbers, name = 'sort_numbers'),
    path('hi/<str:name>/<int:age>',local_views.check_age,name='check_age'),
    
    path('posts/',posts_views.list_posts,name='feed'),

    path('users/login/',users_views.login_view,name='login')
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # Configurado en settings.py para mostrar media durante desarrollo