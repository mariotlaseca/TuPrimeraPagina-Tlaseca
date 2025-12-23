from django.shortcuts import render
from tienda_app.models import *

def home(request):
    return render(request, "tienda_app/index.html")

def lista_de_productos(request):
    productos_query = TiposDeProductos.objects.all()
    contexto = {
        "Productos": productos_query,
    }
    return render(request, "tienda_app/tipos_de_productos.html", contexto)

def lista_de_anillos(request):
    anillos_query = Anillos.objects.all()
    contexto = {
        "Anillos": anillos_query,
    }
    return render(request, "tienda_app/Anillos.html", contexto)

def lista_de_pulseras(request):
    pulseras_query = Pulseras.objects.all()
    contexto = {
        "Anillos": pulseras_query,
    }
    return render(request, "tienda_app/Pulseras.html", contexto)

def lista_de_collares(request):
    collares_query = Collares.objects.all()
    contexto = {
        "Anillos": collares_query,
    }
    return render(request, "tienda_app/Collares.html", contexto)

def lista_de_combinados(request):
    combinados_query = Combinados.objects.all()
    contexto = {
        "Anillos": combinados_query,
    }
    return render(request, "tienda_app/Combinados.html", contexto)

def lista_de_caballeros(request):
    caballeros_query = Caballeros.objects.all()
    contexto = {
        "Anillos": caballeros_query,
    }
    return render(request, "tienda_app/Caballeros.html", contexto)

def lista_de_aretes(request):
    aretes_query = Aretes.objects.all()
    contexto = {
        "Anillos": aretes_query,
    }
    return render(request, "tienda_app/Aretes.html", contexto)