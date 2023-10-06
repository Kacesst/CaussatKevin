from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=32)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=64, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    precio = models.IntegerField()
    talle = models.CharField(max_length=16, default='Sin Talle')
    marca = models.CharField(max_length=100, default='Sin marca')
    modelo = models.CharField(max_length=100, default='Sin modelo')
    foto = models.ImageField(upload_to='productos/', null=True)

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'
    
def buscar_productos(request):
    categoria = request.GET.get('categoria')
    productos = Producto.objects.all()
    if categoria:
        productos = productos.filter(categoria=categoria)
    categorias = Producto.objects.values('categoria').distinct()
    return (request, 'buscar_productos.html', {'productos': productos, 'categorias': categorias})

class Slide(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    link = models.URLField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.producto.nombre 
    
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Si deseas vincular el carrito a usuarios
    productos = models.ManyToManyField('Producto', through='ItemCarrito')

    def agregar_producto(self, producto, cantidad=1):
        # Verificar si el producto ya está en el carrito y actualizar la cantidad
        item, created = ItemCarrito.objects.get_or_create(carrito=self, producto=producto)
        if not created:
            item.cantidad += cantidad
            item.save()

    def quitar_producto(self, producto):
        # Eliminar el producto del carrito
        ItemCarrito.objects.filter(carrito=self, producto=producto).delete()

    def vaciar_carrito(self):
        # Vaciar todo el carrito
        self.productos.clear()

    def __str__(self):
        return f'Carrito de {self.usuario.username}' 

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.producto.nombre} - Cantidad: {self.cantidad}'
    
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