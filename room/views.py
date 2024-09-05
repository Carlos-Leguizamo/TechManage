from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Sala, Computadores
from .forms import SalaForm, ComputadorForm

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
            sala.inventario_cantidad = Computadores.objects.filter(id_sala=sala).count()
            sala.save(update_fields=['inventario_cantidad']) 
            return redirect('pc', sala_id=sala_id)
        elif 'crear' in request.POST:
            if computadores.count() >= sala.capacidad:
                return render(request, 'pc.html', {
                    'sala': sala, 'computadores': computadores, 'form': form, 
                    'error_message': 'No se pueden agregar más computadores. Se ha alcanzado la capacidad máxima de la sala.'
                })
            form = ComputadorForm(request.POST)
            if form.is_valid():
                form.instance.id_sala = sala
                form.save()
                sala.inventario_cantidad = Computadores.objects.filter(id_sala=sala).count()
                sala.save(update_fields=['inventario_cantidad']) 
                return redirect('pc', sala_id=sala_id)
    else:
        form = ComputadorForm()

 

    return render(request, 'pc.html', {'sala': sala, 'computadores': computadores_page, 'form': form, 'error_message': None})
