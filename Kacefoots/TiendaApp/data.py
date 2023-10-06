# TiendaApp/data.py

from .models import Producto, Categoria

def fix_product_category():
    producto = Producto.objects.get(id=1)
    categoria = Categoria.objects.get(nombre="Calzado")  
    producto.categoria = categoria
    producto.save()

Categoria.objects.get_or_create(nombre="Calzado")

fix_product_category()