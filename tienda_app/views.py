from django.shortcuts import render, redirect
from tienda_app.models import *
from tienda_app.forms import *

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
        "Pulseras": pulseras_query,
    }
    return render(request, "tienda_app/Pulseras.html", contexto)

def lista_de_collares(request):
    collares_query = Collares.objects.all()
    contexto = {
        "Collares": collares_query,
    }
    return render(request, "tienda_app/Collares.html", contexto)

def lista_de_combinados(request):
    combinados_query = Combinados.objects.all()
    contexto = {
        "Combinados": combinados_query,
    }
    return render(request, "tienda_app/Combinados.html", contexto)

def lista_de_caballeros(request):
    caballeros_query = Caballeros.objects.all()
    contexto = {
        "Caballeros": caballeros_query,
    }
    return render(request, "tienda_app/Caballeros.html", contexto)

def lista_de_aretes(request):
    aretes_query = Aretes.objects.all()
    contexto = {
        "Aretes": aretes_query,
    }
    return render(request, "tienda_app/Aretes.html", contexto)

def crear_productos(request):
    contexto = {'form':form}
    if request.method == "POST":
        form = TiposDeProductosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = TiposDeProductosForm()
    
    return render(request, 'tienda_app/crear_producto.html',contexto)

def crear_anillos(request):
    contexto = {'form':form}
    if request.method == "POST":
        form = AnillosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("anillos_list")
    else:
        form = AnillosForm()
    
    return render(request, 'tienda_app/crear_anillos.html',contexto)

def crear_pulseras(request):
    contexto = {'form':form}
    if request.method == "POST":
        form = PulserasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pulseras_list")
    else:
        form = PulserasForm()
    
    return render(request, 'tienda_app/crear_pulseras.html',contexto)

def crear_collares(request):
    contexto = {'form':form}
    if request.method == "POST":
        form = CollaresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("collares_list")
    else:
        form = CollaresForm()
    
    return render(request, 'tienda_app/crear_collares.html',contexto)

def crear_combinados(request):
    contexto = {'form':form}
    if request.method == "POST":
        form = CombinadosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("combinados_list")
    else:
        form = CombinadosForm()
    
    return render(request, 'tienda_app/crear_combinados.html',contexto)

def crear_caballeros(request):
    contexto = {'form':form}
    if request.method == "POST":
        form = CaballerosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("caballeros_list")
    else:
        form = CaballerosForm()
    
    return render(request, 'tienda_app/crear_caballeros.html',contexto)

def crear_aretes(request):
    contexto = {'form':form}
    if request.method == "POST":
        form = AretesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("aretes_list")
    else:
        form = AretesForm()
    
    return render(request, 'tienda_app/crear_aretes.html',contexto)