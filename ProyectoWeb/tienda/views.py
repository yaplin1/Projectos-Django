from django.shortcuts import render, get_object_or_404
from .models import Producto, CategoriaProd

# Create your views here.

def tienda(request):

    productos=Producto.objects.filter(disponibilidad=True)
    categorias=CategoriaProd.objects.all()

    return render(request, "tienda/tienda.html", {"productos":productos, "categorias": categorias})

def productos_por_categoria(request, categorias_id):

    categoria=get_object_or_404(CategoriaProd, id=categorias_id)
    productos=Producto.objects.filter(categorias=categoria, disponibilidad=True)
    return render(request, "tienda/productos_por_categoria.html", {'categoria_actual':categoria,'productos': productos, 'categorias_disponibles': CategoriaProd.objects.all() })

# Nueva vista para el buscador
def buscar_productos(request):
    query = request.GET.get('q')
    #print("Valor recibido:", query)  # <-- Esto te ayuda a depurar
    productos = Producto.objects.all() # Traer todos los productos por defecto

    if query:
        # Usamos Q objects para buscar en nombre o en la descripción del producto
        productos = productos.filter(
            Q(nombre__icontains=query) 
        ).distinct()

    return render(request, 'tienda/resultados_busqueda.html', {'productos': productos, 'query': query})
