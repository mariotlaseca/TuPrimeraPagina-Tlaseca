from django.urls import path
from tienda_app.views import *

urlpatterns = [
    path("", home, name = "home"),
    path("tipos_de_productos", lista_de_productos, name="product_list"),
    path("Anillos", lista_de_anillos, name="anillos_list"),
    path("Pulseras", lista_de_pulseras, name="pulseras_list"),
    path("Collares", lista_de_collares, name = "collares_list"),
    path("Combinados", lista_de_combinados, name="combinados_list"),
    path("Caballeros", lista_de_caballeros, name="caballeros_list"),
    path("Aretes", lista_de_aretes, name="aretes_list"),
]