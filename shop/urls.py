from django.urls import path
from . import views

urlpatterns = [
     path('compras/', views.compras, name='compras'),
     path('comprar/<int:producto_id>/', views.comprar_producto, name='comprar_producto'),
]