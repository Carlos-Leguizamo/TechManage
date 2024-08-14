from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # Clase de Django para los formularios de registro y login
from django.contrib.auth.models import User  # Clase para registrar usuarios
from django.contrib.auth import login, logout, authenticate # Crea la cookies en el navegador
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required #Seguridad de las rutas y no permitir acceso mediantre ellas si no esta logueado

# Create your views here.


def home(request):
    return render(request, "home.html")

# Logica de registro de Usuarios
def register(request):

    if request.method == "GET":
        return render(request, "signup.html", {
            "formRegister": UserCreationForm
            })

    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                # registrar usuario

                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )

                user.save()  # Guardar usuario registrdo en la BD
                login(request, user)  # Iniciar sesión del usuario
                return redirect('dashboard')

            except IntegrityError:
                return render(request, "signup.html", {
                    "formRegister": UserCreationForm,
                    'error': 'El usuario ya existe'
            })
               

        return render(request, "signup.html", {
                    "formularioRegistro": UserCreationForm,
                    'error': 'Contraseñas no coinciden'
            })
    
#Seguridad de la ruta  
@login_required
def dashboard(request):
    return render(request, "dashboard.html")
# Logica de Logout o cerrrar sesion 
def signout (request):
    logout(request)
    return redirect('home')

# Logica de inicio de sesión}
def signin (request):
    if request.method == "GET":
        return render(request, "signin.html", {
            "formLogin": AuthenticationForm
            })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:    
            return render(request, "signin.html", {
                "formLogin": AuthenticationForm,  
                "error":'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)  # Iniciar sesión del usuario - Guaradar sesion del usuario
            return redirect('dashboard')
       
        
          


