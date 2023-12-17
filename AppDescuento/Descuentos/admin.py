
from django.contrib import admin
from .models import Producto

admin.site.register(Producto)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'descuento')