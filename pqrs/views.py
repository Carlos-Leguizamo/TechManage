from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from .models import PQRS
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import PQRSForm
from django.core.paginator import Paginator


# Logica para retornar la vista de PQRS


#Flujo para el registro del PQRS en la BD


@login_required
def view_pqrs(request):
    # Verificamos si el usuario ya tiene un PQRS pendiente
    if PQRS.objects.filter(estado='pendiente', usuario=request.user).exists():
        messages.error(request, 'Ya tienes una solicitud PQRS pendiente. Por favor, espera a que el administrador la resuelva antes de enviar una nueva.')
        return redirect('view-pending-pqrs')  # Redirigir a la vista de PQRS pendientes

    if request.method == 'POST':
        form = PQRSForm(request.POST)
        if form.is_valid():
            pqrs = form.save(commit=False)
            pqrs.fecha_creacion = timezone.now()  
            pqrs.estado = 'pendiente'  
            pqrs.usuario = request.user  # Asociamos el usuario logueado o actual
            pqrs.save()  
            # messages.success(request, 'Su solicitud PQRS ha sido creada con éxito.')
            return redirect('view-pending-pqrs') 
    else:
        form = PQRSForm()

    context = {
        'form': form,
        'TIPO_CHOICES': PQRS.TIPO_CHOICES  # Pasar las opciones de tipo a la plantilla
    }
    return render(request, 'pqrs.html', context)

@login_required
def pending_pqrs(request):
    pqrs_pendientes = PQRS.objects.filter(estado='pendiente', usuario=request.user)  # Cambiar 'id' a 'usuario'
    context = {
        'pqrs_pendientes': pqrs_pendientes,
    }
    return render(request, 'pending-pqrs.html', context)

@login_required
def admin_pqrs(request):
    pqrs = PQRS.objects.all()
    paginator = Paginator(pqrs, 5)
    page_number = request.GET.get("page")
    pqrs_list = paginator.get_page(page_number)
    
    context = {
        'pqrs_list': pqrs_list
    }
    return render(request, 'admin-pqrs.html', context)



@login_required
def confirm_delete_pqrs(request, id):
    # Usar 'id' para obtener el objeto PQRS
    pqrs = get_object_or_404(PQRS, id_pqrs=id)  # Cambia 'id' por 'id_pqrs'
    
    if request.method == 'POST':
        print("Método POST recibido.")
        pqrs.delete()
        messages.success(request, 'La PQRS ha sido eliminada con éxito.')
        return redirect('view-admin-pqrs')

    return render(request, 'confirm_delete_pqrs.html', {'pqrs': pqrs})

@login_required
def check_pqrs(request, id):
    pqrs = get_object_or_404(PQRS, id_pqrs=id)  # Usa 'id_pqrs' aquí
    return render(request, 'confirm-check-pqrs.html', {'pqrs': pqrs})
