from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import UserEditForm, ProductoForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from TiendaApp.Carrito import Carrito
from TiendaApp.models import Producto
from .models import Comprador, Pedido, DetallePedido, Producto, Categoria
from django.contrib.auth.models import User
from .Carrito import Carrito
from .data import *


def inicio(request):
    return render(request, 'inicio.html') 


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    
    return render(request, 'crear_producto.html', {'form': form})

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'editar_producto.html', {'form': form})


 
def restar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = Carrito(request)
    carrito.restar(producto)
    return redirect('carrito')  

def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos':productos})

def carrito(request):
    carrito = Carrito(request)
    productos_en_carrito = carrito.carrito.values()
    total_carrito = sum(item['acumulado'] for item in productos_en_carrito)
    return render(request, 'carrito.html', {'productos': productos_en_carrito, 'total_carrito': total_carrito})


def productos(request):

  # Filtros
  nombre = request.GET.get('nombre') 
  categoria = request.GET.get('categoria')

  # Consulta
  productos = Producto.objects.filter(
      nombre__contains=nombre,
      categoria=categoria
  )

  # Paginación 
  productos = productos.paginate(page=request.GET.get('page', 1))

  return render(request, 'lista_productos.html', {
    'productos': productos
  })

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})


def buscar_productos(request):
    categoria_id = request.GET.get('categoria')
    productos = Producto.objects.all()
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    categorias = Categoria.objects.all()
    return render(request, 'buscar_productos.html', {'productos': productos, 'categorias': categorias})

@login_required
def agregar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito = Carrito(request)
    carrito.agregar(producto)
    return redirect('carrito')

@login_required
def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito = Carrito(request)
    carrito.eliminar(producto)
    return redirect('carrito')

@login_required
def restar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito = Carrito(request)
    carrito.restar(producto)
    return redirect('carrito')

@login_required
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('carrito')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('inicio')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

@login_required
def signout(request):
    logout(request)
    return redirect('inicio')



def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio')
    else:
        form = AuthenticationForm()

    return render(request, 'signin.html', {'form': form})
    
def about (req):
    return render (req, "about.html" )

def fame(req):
    if req.method == 'POST':
        form = ProductoForm(req.POST)
        if form.is_valid():
            producto_seleccionado = form.cleaned_data['producto']
            return render(req, 'fame.html', {'producto': producto_seleccionado})
    else:
        form = ProductoForm()

    return render(req, "fame.html", {'form': form})
    
def contacto (req):
    return render (req, "contato.html" )
    

def editar_perfil(req):
    if req.method == 'POST':
        miFormulario = UserEditForm(req.POST, instance=req.user)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = req.user
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()
            return
    
    
def perfil_comprador(request):
    comprador = get_object_or_404(Comprador, usuario=request.user)
    return render(request, 'perfil_comprador.html', {'comprador': comprador})

def mis_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user)
    return render(request, 'mis_pedidos.html', {'pedidos': pedidos})

def detalle_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, usuario=request.user)
    detalles = DetallePedido.objects.filter(pedido=pedido)
    return render(request, 'detalle_pedido.html',
    {'pedido': pedido, 'detalles': detalles})
    

 


