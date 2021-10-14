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
from django.urls import path, include

"""
Librerias para poder visualizar imagenes o media desde el panel de administracion.
"""
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls, name = 'admin'),

    path('',include(('posts.urls','posts'),namespace='posts')),
    path('users/',include(('users.urls','users'),namespace='users')),
    
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # Configurado en settings.py para mostrar media durante desarrollo