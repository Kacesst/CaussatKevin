"""Carrito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from TiendaApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'), 
    path('tienda/', include('TiendaApp.urls')),
    path('about/', about, name='about'),
    path('contacto/', contacto, name='contacto'),
    path('logout/', signout, name='logout'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('tienda/', tienda, name='tienda'),
    path('fame/', fame, name='fame'),
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('editar_producto/<int:pk>/', editar_producto, name='editar_producto'),
    path('restar_producto/<int:producto_id>/', restar_producto, name='restar_producto'),
    path('carrito/', carrito, name='carrito'),
    path('lista_productos/', lista_productos, name='lista_productos'),
    path('agregar_producto/<int:producto_id>/', agregar_producto, name='agregar_producto'),
    path('eliminar_producto/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    path('limpiar_carrito/', limpiar_carrito, name='CLS'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('perfil_comprador/', perfil_comprador, name='perfil_comprador'),
    path('mis_pedidos/', mis_pedidos, name='mis_pedidos'),
    path('detalle_pedido/<int:pedido_id>/', detalle_pedido, name='detalle_pedido'),   
    path('agregar_producto/<int:producto_id>/', agregar_producto, name='agregar_producto'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    