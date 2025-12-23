from django.urls import path
from tienda_app.views import *

urlpatterns = [
    path("", home, name = "home"),
    path("tipos_de_productos", lista_de_productos, name="product_list"),
]