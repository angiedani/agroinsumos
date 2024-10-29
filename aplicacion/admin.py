from django.contrib import admin
from .models import Categoria, Producto  # Asegúrate de importar tus modelos correctamente

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('idCategoria', 'nomCategoria', 'subcategoria', 'imagen')
    search_fields = ('nomCategoria',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('idProducto', 'nomProducto', 'precioProducto', 'stock', 'categoria', 'imagen')
    search_fields = ('nomProducto',)
    list_filter = ('categoria',)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
