# Django
from django.contrib import admin

# Models
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Profile admin"""
    list_display = ('pk','user','title') # Campos que debe mostrar en el display de admin
    list_display_links=('pk','user','title') # Elementos linkados al detalle
    
    # Creamos un buscador de usuarios segun los siguientes campos
    search_fields = (
        'user__username',
        'title'
        
    )

    # Creamos un filtro con los siguientes campos
    
    list_filter = (
        'created',
        'modified',
    )

    # Si queremos especificar que campos pueden modificarse desde el dashboard de Djando Admin usams fieldsets

    readonly_fields = ('created','modified','user') # Evita que estos campos se puedan modificar en el dashboard. Además evita que se generen errores al ser 'created' un campo no editable

