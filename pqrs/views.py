from django.shortcuts import render,redirect
from django.contrib import messages
from .models import PQRS
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import PQRSForm


# Logica para retornar la vista de PQRS


#Flujo para el registro del PQRS en la BD
def view_pqrs(request):
    if request.method == 'POST':
        form = PQRSForm(request.POST)
        if form.is_valid():
            pqrs = form.save(commit=False)
            pqrs.fecha_creacion = timezone.now()  # Establecer la fecha de creación
            pqrs.estado = 'pendiente'  # Establecer el estado por defecto
            pqrs.usuario = request.user  # Asociar el usuario actual
            pqrs.save()  # Guardar el objeto en la base de datos
            messages.success(request, 'Su solicitud PQRS ha sido creada con éxito.')
            return redirect('view-pending-pqrs')  # Redirigir a la vista de PQRS pendientes
    else:
        form = PQRSForm()

    context = {
        'form': form,
        'TIPO_CHOICES': PQRS.TIPO_CHOICES  # Pasar las opciones de tipo a la plantilla
    }
    return render(request, 'pqrs.html', context)

def pending_pqrs(request):
    pqrs_pendientes = PQRS.objects.filter(estado='pendiente', usuario=request.user)  # Cambiar 'id' a 'usuario'
    context = {
        'pqrs_pendientes': pqrs_pendientes,
    }
    return render(request, 'pending-pqrs.html', context)

