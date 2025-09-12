from django.contrib import admin
from .models import CategoriaProd, Producto

# Register your models here.

class CategoriaProdAdmin(admin.ModelAdmin):

    readonly_fields=('created', 'updated')

class ProductoAdmin(admin.ModelAdmin):

    search_fields=('nombre', 'categorias__nombre')
    list_display=('nombre', 'categorias', 'precio', 'disponibilidad')
    readonly_fields=('created', 'updated')

admin.site.register(CategoriaProd, CategoriaProdAdmin)

admin.site.register(Producto, ProductoAdmin)

