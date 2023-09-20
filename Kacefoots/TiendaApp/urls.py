from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('productos/', views.productos, name='productos'),
path('perfil/', views.perfil_comprador, name='perfil'),
path('pedidos/', views.mis_pedidos, name='pedidos'),
path('pedido/int:pedido_id/', views.detalle_pedido, name='detalle_pedido')
]

