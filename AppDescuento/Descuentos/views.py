from django.shortcuts import render
from .models import Producto

def index(request):
    # Lógica para la página principal (index.html)
    return render(request, 'index.html')

def en_construccion(request):
    # Lógica para la página "En construcción"
    return render(request, 'en_construccion.html')

def profile(request):
    return render(request, 'profile.html')

def manual_usuario(request):
    # Lógica para la página del manual de usuario
    return render(request, 'manual.html')

def lista_productos(request):
    # Obtener todos los productos desde la base de datos
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def buscar_descuentos(request):
    query = request.GET.get('q', '')
    productos_con_descuento = Producto.objects.filter(nombre__icontains=query, descuento__gt=0)
    return render(request, 'buscar_descuentos.html', {'productos': productos_con_descuento})

def carrito_de_compras(request):
    return render(request, 'carrito_de_compras.html', context={})

def buscar_productos(request):
    categoria = request.GET.get('categoria', '')
    productos = Producto.objects.filter(categoria=categoria)
    return render(request, 'lista_productos.html', {'productos': productos})

def manual_usuario(request):
    return render(request, 'manual_usuario.html')
# views.py

from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            # Mensaje de error
            pass
    return render(request, 'login.html')

# En tu archivo views.py
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login as auth_login

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')  # Redirige a la página de inicio después del registro
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

from django.contrib import messages

from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout

def custom_logout(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Has cerrado sesión, nos vemos pronto')
    return redirect('index')


@csrf_exempt
def enviar_correo(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')  # Usar un valor predeterminado en caso de que no haya email
        if email:
            send_mail(
                'Felicidades ya eres parte de Aplicacion de Descuento',
                'Felicidades ya eres parte de Aplicacion de Descuento, te estaremos informando sobre las mejores ofertas según tus intereses.',
                'appdescuentos19@gmail.com',
                [email],
                fail_silently=False,
            )
            return HttpResponse("Correo enviado a " + email)
        else:
            return HttpResponse("No se proporcionó una dirección de correo electrónico.")
    else:
        return HttpResponse("Solicitud no válida.")