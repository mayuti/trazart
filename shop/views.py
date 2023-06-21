from django.shortcuts import render, redirect
from .models import Producto


# Create your views here.

def compras(request):
    productos = Producto.objects.all()
    return render(request, 'compras.html', {'productos': productos})

def comprar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return redirect('compras')