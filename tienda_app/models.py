from django.db import models

class TiposDeProductos(models.Model):
    tipo = models.CharField(max_length=50)
    identificador = models.IntegerField(unique=True)
    fecha_de_actualizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} \nActualizado: {self.fecha_de_actualizacion}" 
