from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Sala, Computadores
from .forms import SalaForm, ComputadorForm
import schedule
import time
import threading
from datetime import datetime, timedelta
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

def sala(request):
    form = None
    sala_id = None
    if request.method == 'POST':
        if 'editar' in request.POST:
            sala_id = request.POST.get('sala_id')
            sala = get_object_or_404(Sala, id_sala=sala_id)
            form = SalaForm(request.POST, instance=sala)
            if form.is_valid():
                form.save()
                return redirect('sala')
        elif 'eliminar' in request.POST:
            sala_id = request.POST.get('sala_id')
            sala = get_object_or_404(Sala, id_sala=sala_id)
            sala.delete()
            return redirect('sala')
        elif 'crear' in request.POST:
            form = SalaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('sala')
    else:
        sala_id = request.GET.get('sala_id')
        if sala_id:
            sala = get_object_or_404(Sala, id_sala=sala_id)
            form = SalaForm(instance=sala)
        else:
            form = SalaForm()
    
    salas = Sala.objects.all()
    for sala in salas:
        sala.inventario_cantidad = Computadores.objects.filter(id_sala=sala).count()
        sala.save(update_fields=['inventario_cantidad']) 

    paginator = Paginator(salas, 4) 
    page = request.GET.get('page')
    try:
        salas_page = paginator.page(page)
    except PageNotAnInteger:
        salas_page = paginator.page(1)
    except EmptyPage:
        salas_page = paginator.page(paginator.num_pages)

    return render(request, 'sala.html', {'salas': salas_page, 'form': form, 'edit': sala_id is not None})

def pc(request, sala_id):
    sala = get_object_or_404(Sala, id_sala=sala_id)
    computadores = Computadores.objects.filter(id_sala=sala)

    paginator = Paginator(computadores, 4) 
    page = request.GET.get('page')
    try:
        computadores_page = paginator.page(page)
    except PageNotAnInteger:
        computadores_page = paginator.page(1)
    except EmptyPage:
        computadores_page = paginator.page(paginator.num_pages)

    form = None

    if request.method == 'POST':
        if 'editar' in request.POST:
            pc_id = request.POST.get('pc_id')
            computador = get_object_or_404(Computadores, id_computador=pc_id)
            form = ComputadorForm(request.POST, instance=computador)
            if form.is_valid():
                form.save()
                return redirect('pc', sala_id=sala_id)
        elif 'eliminar' in request.POST:
            pc_id = request.POST.get('pc_id')
            computador = get_object_or_404(Computadores, id_computador=pc_id)
            computador.delete()
            # Actualiza el conteo de computadores en la sala tras la eliminación
            sala.inventario_cantidad = Computadores.objects.filter(id_sala=sala).count()
            sala.save(update_fields=['inventario_cantidad']) 
            # Redirige tras la eliminación para evitar reenvíos accidentales del formulario
            return redirect('pc', sala_id=sala_id)
        elif 'crear' in request.POST:
            # Verifica si la capacidad de la sala ha sido alcanzada
            if computadores.count() >= sala.capacidad:
                return render(request, 'pc.html', {
                    'sala': sala, 'computadores': computadores_page, 'form': form, 
                    'error_message': 'No se pueden agregar más computadores. Se ha alcanzado la capacidad máxima de la sala.'
                })
            form = ComputadorForm(request.POST)
            if form.is_valid():
                form.instance.id_sala = sala
                form.save()
                # Actualiza el conteo de computadores tras la creación
                sala.inventario_cantidad = Computadores.objects.filter(id_sala=sala).count()
                sala.save(update_fields=['inventario_cantidad']) 
                return redirect('pc', sala_id=sala_id)
    else:
        form = ComputadorForm()

    return render(request, 'pc.html', {
        'sala': sala,
        'computadores': computadores_page, 
        'form': form,
        'error_message': None
    })

def verificar_mantenimiento():
    # Obtiene la hora actual
    ahora = timezone.now()
    
    # Obtén todos los computadores
    computadores = Computadores.objects.all()

    for computador in computadores:
        # Verifica si la fecha de mantenimiento es hoy o ya pasó
        if computador.mantenimiento_programado <= ahora:
            sala = computador.id_sala
               # Determina el artículo correcto según el tipo de computador
            if computador.tipo.lower() == "laptop":
                articulo = "la laptop"
            else:
                articulo = "el computador"

            mensaje = (f"Es hora de realizar el mantenimiento para {articulo} de marca {computador.marca} "
                       f"y modelo {computador.modelo}. Está ubicado en la sala: {sala.nombre_sala}, "
                       f"ubicación: {sala.ubicacion}.")
            print(mensaje)  # Puedes seguir imprimiendo el mensaje en consola para registro

            # Envía un correo electrónico
            send_mail(
                'Recordatorio de Mantenimiento',
                mensaje,
                settings.DEFAULT_FROM_EMAIL, 
                ['santiagofiriguapalma@gmail.com'] 
            )

            # Actualiza la fecha de mantenimiento a 6 meses a partir de ahora
            computador.mantenimiento_programado = ahora + timedelta(days=180)  # 6 meses = 180 días
            computador.save(update_fields=['mantenimiento_programado'])

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)  # Espera un minuto antes de volver a verificar

# Programa la tarea cada minuto
schedule.every().minute.do(verificar_mantenimiento)

# Inicia el hilo para ejecutar el programador de tareas
threading.Thread(target=run_schedule, daemon=True).start()