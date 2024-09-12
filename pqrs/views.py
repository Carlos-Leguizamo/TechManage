from django.shortcuts import render,redirect
from django.contrib import messages
from .models import PQRS
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import PQRSForm


# Logica para retornar la vista de PQRS

def view_pqrs(request):
    # Si la solicitud se hace a traves del metodo POST
    if request.method == 'POST':
        form = PQRSForm(request.POST)
        if form.is_valid():
            pqrs = form.save(commit=False)
            pqrs.fecha_creacion = timezone.now()  # Establecer la fecha de creación
            pqrs.id = request.user  # Asociar el usuario (id) actual
            pqrs.save()
            messages.success(request, 'Su solicitud PQRS ha sido creada con éxito.')
            return redirect('success_url')  # Url a redirigir kluiego de validad y guardadr los daots en la BD 
    else:
        form = PQRSForm()

    context = {
        'form': form,
        'TIPO_CHOICES': PQRS.TIPO_CHOICES  # Pasar las opciones de tipo (Queja, Peticion, etc..) a la plantilla
    }
    return render(request, 'pqrs.html', context)

