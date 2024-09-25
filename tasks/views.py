from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # Clase de Django para los formularios de registro y login
from django.contrib.auth.models import User  # Clase para registrar usuarios
from django.contrib.auth import login, logout, authenticate # Crea la cookies en el navegador
from django.db import IntegrityError
import random
import string
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils import timezone
from django.conf import settings
from .models import TokenVerification
from .decorators import validacion_requerida
from .decorators import token_requerido
from users.models import UserProfile
import uuid

# Variables globales para el token y su expiración
VERIFICATION_TOKEN = None
TOKEN_EXPIRATION = None


# Create your views here.


def home(request):
    return render(request, "home.html")


# Logica de registro de Usuarios

@validacion_requerida 
def register(request):
    if request.method == "GET":
        return render(request, "signup.html", {
            "formRegister": UserCreationForm()
        })

    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                # Verificar si el correo ya está registrado
                if User.objects.filter(email=request.POST["email"]).exists():
                    return render(request, "signup.html", {
                        "formRegister": UserCreationForm(),
                        'error': 'El correo electrónico ya está en uso'
                    })
    
                # Registrar usuario
                user = User.objects.create_user(
                    username=request.POST["username"],
                    first_name=request.POST["first_name"],
                    last_name=request.POST["last_name"],
                    email=request.POST["email"],
                    password=request.POST["password1"],
                )
                
                # Crear perfil de usuario y asignar el token
                # UserProfile.objects.create(user=user, token_verification=str(uuid.uuid4()))

                user.save()  # Guardar usuario registrado en la BD
                login(request, user)  # Iniciar sesión del usuario
                # Comentando la línea para depuración
                # request.session['validado'] = False
                return redirect('dashboard')

            except IntegrityError:
                return render(request, "signup.html", {
                    "formRegister": UserCreationForm(),
                    'error': 'El nombre de usuario ya existe'
                })

        return render(request, "signup.html", {
            "formRegister": UserCreationForm(),
            'error': 'Las contraseñas no coinciden'
        })

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



#LOGICA DE ENVIO DE TOKEN PARA PASAR AL FORMULARIO DE RESGITRO 



#Logica de generar codigo de manera ramdon con la libreria ramdon
def generate_token():
    #Genera un token de 6 caracteres.
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


#Logica de envio de codigo por medio de email 

def send_verification_email(request):
    if request.method == 'POST':
        token = generate_token()
        expiration = timezone.now() + timezone.timedelta(minutes=5)
        TokenVerification.objects.create(token=token, expiration=expiration)
        
        send_mail(
            'Código de verificación',
            f'Este es tu código de verificación: {token}',
            settings.DEFAULT_FROM_EMAIL,
            ['eldermoreno450@gmail.com']
        )
        request.session['token_verificado'] = True
        return redirect('verify_token')
    return render(request, 'send_token.html')

# Logica para verificar token

@token_requerido
def verify_token_view(request):
    if request.method == 'POST':
        token = request.POST.get('token')
        try:
            verification_token = TokenVerification.objects.get(token=token)
            if verification_token.is_valid():
                verification_token.delete()  # Elimina el token después de la verificación
                request.session['validado'] = True  # Marca como validado en la sesión
                request.session['token_verificado'] = False  # Restablecer a False después del registro
                
                return redirect('register')
            else:
                return render(request, 'verify_token.html', {'error': 'Código expirado'})
        except TokenVerification.DoesNotExist:
            return render(request, 'verify_token.html', {'error': 'Código inválido'})
    return render(request, 'verify_token.html')
    


