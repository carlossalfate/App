"""
URL configuration for AppDescuento project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from Descuentos import views
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    path('productos/', views.lista_productos, name='lista_productos'),
    path('manual-usuario/', views.manual_usuario, name='manual_usuario'),
    path('buscar_descuentos/', views.buscar_descuentos, name='buscar_descuentos'),
    path('carrito_de_compras/', views.carrito_de_compras, name='carrito_de_compras'),
    path('buscar_productos/', views.buscar_productos, name='buscar_productos'),
    path('buscar_descuentos/', views.buscar_descuentos, name='buscar_descuentos'),
    path('enviar_correo/', views.enviar_correo, name='enviar_correo'),
    path('manual/', views.manual_usuario, name='manual_usuario'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile'),
    path('logout/', views.custom_logout, name='logout'),
]   

