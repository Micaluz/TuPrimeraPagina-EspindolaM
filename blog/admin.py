from django.contrib import admin
from .models import Autor, Categoria, Post

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'fecha')
    list_filter = ('categoria', 'autor')
    search_fields = ('titulo', 'contenido')
