# Importa la configuración de Django para que puedas acceder a tus modelos
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Kacefoots.settings")
django.setup()

# Importa el modelo de Categoria desde tu aplicación
from TiendaApp.models import Categoria

# Lista de categorías a crear
categorias_a_crear = ['Ropa', 'Accesorios', 'Electrónicos']

# Itera sobre la lista y crea las categorías si no existen
for categoria_nombre in categorias_a_crear:
    categoria, created = Categoria.objects.get_or_create(nombre=categoria_nombre)
    if created:
        print(f"Se ha creado la categoría '{categoria_nombre}'")
    else:
        print(f"La categoría '{categoria_nombre}' ya existe")

# Sal del script
exit()
