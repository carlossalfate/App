from django.db import models
from django.shortcuts import render

class Descuento(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50)  # Porcentaje, Fijo, BOGO (compra uno y obtén otro gratis)
    valor = models.IntegerField()  # Cambiado a IntegerField
    productos = models.ManyToManyField('Producto', related_name='descuentos', blank=True)

def lista_productos(request):
    productos = Producto.objects.all()  # Recupera todos los productos de la base de datos
    return render(request, 'tu_app/lista_productos.html', {'productos': productos})

def buscar_productos(request):
    categoria = request.GET.get('categoria', '')
    productos = Producto.objects.filter(categoria=categoria)
    return render(request, 'lista_productos.html', {'productos': productos})

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()  # Cambiado a IntegerField
    categoria = models.CharField(max_length=100)
    descuento = models.IntegerField(blank=True, null=True)  # Cambiado a IntegerField
    imagen_nombre = models.CharField(max_length=100, blank=True)
    # Otros campos que puedas necesitar para tu producto

class Suscripcion(models.Model):
    correo_electronico = models.EmailField()
    categoria_interes = models.CharField(max_length=100)

def buscar_descuentos(request):
    query = request.GET.get('q', '')
    productos_con_descuento = Producto.objects.filter(nombre__icontains=query, descuento__gt=0)
    return render(request, 'lista_descuentos.html', {'productos': productos_con_descuento})

from django.contrib.auth.models import AbstractBaseUser

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    # otros campos

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

def __str__(self):
    return self.nombre
