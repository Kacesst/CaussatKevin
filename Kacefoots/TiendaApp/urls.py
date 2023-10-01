from django.urls import include, path
from . import views
from TiendaApp.views import *

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('fame/', views.fame, name='fame'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('editar_producto/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('restar_producto/<int:producto_id>/', views.restar_producto, name='restar_producto'),
    path('carrito/', views.carrito, name='carrito'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('agregar_producto/<int:producto_id>/', views.agregar_producto, name='agregar_producto'),
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('limpiar_carrito/', views.limpiar_carrito, name='limpiar_carrito'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('perfil_comprador/', views.perfil_comprador, name='perfil_comprador'),
    path('mis_pedidos/', views.mis_pedidos, name='mis_pedidos'),
    path('detalle_pedido/<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),   
    
]

urlpatterns = [
    path('tienda/', include(urlpatterns)),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)