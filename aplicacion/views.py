from django.shortcuts import render
from .models import Producto  # Importa el modelo de categoría
from .models import Categoria 
# Create your views here.
def index(request):
    productos_destacados = Producto.objects.all()[:4]  # Obtiene los primeros tres productos
    return render(request, 'index.html', {'productos_destacados': productos_destacados})

def vista_categorias(request):
    categorias = Categoria.objects.all()  # Obtiene todas las categorías
    return render(request, 'categorias.html', {'categorias': categorias})
