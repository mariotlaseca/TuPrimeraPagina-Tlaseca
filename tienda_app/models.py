from django.db import models

class TiposDeProductos(models.Model):
    tipo = models.CharField(max_length=50)
    identificador = models.IntegerField(unique=True)
    fecha_de_actualizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} \nActualizado: {self.fecha_de_actualizacion}" 

class Anillos(models.Model):
    nombre = models.CharField(max_length=30)
    numero = models.IntegerField(unique=True)
    unidades = models.IntegerField(null=False)
    precio = models.IntegerField(null=False)
    fecha_de_actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} \nPrecio: {self.precio}" 

class Pulseras(models.Model):
    nombre = models.CharField(max_length=30)
    numero = models.IntegerField(unique=True)
    unidades = models.IntegerField(null=False)
    precio = models.IntegerField(null=False)
    fecha_de_actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} \nPrecio: {self.precio}" 

class Collares(models.Model):
    nombre = models.CharField(max_length=30)
    numero = models.IntegerField(unique=True)
    unidades = models.IntegerField(null=False)
    precio = models.IntegerField(null=False)
    fecha_de_actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} \nPrecio: {self.precio}" 

class Combinados(models.Model):
    nombre = models.CharField(max_length=30)
    numero = models.IntegerField(unique=True)
    unidades = models.IntegerField(null=False)
    precio = models.IntegerField(null=False)
    fecha_de_actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} \nPrecio: {self.precio}" 

class Caballeros(models.Model):
    nombre = models.CharField(max_length=30)
    numero = models.IntegerField(unique=True)
    unidades = models.IntegerField(null=False)
    precio = models.IntegerField(null=False)
    fecha_de_actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} \nPrecio: {self.precio}" 

class Aretes(models.Model):
    nombre = models.CharField(max_length=30)
    numero = models.IntegerField(unique=True)
    unidades = models.IntegerField(null=False)
    precio = models.IntegerField(null=False)
    fecha_de_actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} \nPrecio: {self.precio}" 