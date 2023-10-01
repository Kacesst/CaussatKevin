from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=32)
    precio = models.IntegerField()
    talle = models.CharField(max_length=16, default='Sin Talle')
    marca = models.CharField(max_length=100, default='Sin marca')
    modelo = models.CharField(max_length=100, default='Sin modelo')
    foto = models.ImageField(upload_to='productos/', null=True)
    def __str__(self):
        return f'{self.nombre} -> {self.precio}'
    

class Comprador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=255)
    dni = models.IntegerField()
    codigo_postal = models.IntegerField()

    def __str__(self):
        return self.user.username
    

class Pedido(models.Model):
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
   

    def __str__(self):
        return f"Pedido #{self.pk}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return f"Detalle de Pedido #{self.pedido.pk}: {self.producto}"