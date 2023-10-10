# TiendaApp/data.py

from .models import Producto, Categoria

def create_categories():

    # Crear categoría principal
    principal = Categoria.objects.create(nombre="Ropa")  

    # Crear subcategoría
    sub = Categoria.objects.create(
        nombre="Camisas",
        padre=principal
    )

    # Agregar cualquier otra categoría
    Categoria.objects.create(nombre="Pantalones")


def fix_product_category():

    producto = Producto.objects.get(id=1)
    categoria = Categoria.objects.get(nombre="Calzado")   
    producto.categoria = categoria
    producto.save()

def run():
    create_categories()
    fix_product_category()