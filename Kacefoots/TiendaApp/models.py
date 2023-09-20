from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=32)
    precio = models.IntegerField()
    talle = models.CharField(max_length=16)
    marca = models.CharField(max_length=64)
    modelo = models.CharField(max_length=64)
    foto = models.ImageField(upload_to='productos/')
    def __str__(self):
        return f'{self.nombre} -> {self.precio}'