from django.db import models

# Create your models here.

class Producto(models.Model):
    item = models.CharField(max_length=100)
    detalle = models.TextField()
    foto = models.ImageField(upload_to='static/images')
    precio = models.DecimalField(max_digits=8, decimal_places=2)

