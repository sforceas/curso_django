"""Posts models"""

# Django
from django.db import models
from django.contrib.auth.models import User

# Users


# Create your models here.

class Post(models.Model):
    """Post model"""

    user = models.ForeignKey(User,on_delete=models.CASCADE) #CASCADE elimina los posts si se elimina el usuario, PROTECT no elimina los datos al eliminar el usuario, SET_NULL, mantiene los datos pero elimina el nombre de usuario. Depende de cada caso.
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE) # Tambien podemos llamar a los modelos usando la sintaxis 'app.Modelo' en lugar de importar.

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        # Return email
        return 'f{title} by @{user}'