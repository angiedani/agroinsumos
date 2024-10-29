from django.shortcuts import render
from .models import Categoria  # Importa el modelo de categoría

# Create your views here.
def index(request):
  return render(request, 'index.html',{})

def vista_categorias(request):
    categorias = Categoria.objects.all()  # Obtiene todas las categorías
    return render(request, 'categorias.html', {'categorias': categorias})
