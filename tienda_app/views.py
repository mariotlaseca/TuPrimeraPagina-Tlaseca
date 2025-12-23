from django.shortcuts import render
from tienda_app.models import TiposDeProductos

def home(request):
    return render(request, "tienda_app/index.html")

def lista_de_productos(request):
    productos_query = TiposDeProductos.objects.all()
    contexto = {
        "Productos": productos_query,
    }
    return render(request, "tienda_app/tipos_de_productos.html", contexto)