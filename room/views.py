from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Sala
from .forms import SalaForm  
from .models import Computadores
from .forms import ComputadoresForm

#@login_required  
def sala(request):
    form = None  # Inicializa la variable form

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
    return render(request, 'sala.html', {'salas': salas, 'form': form, 'edit': sala_id is not None})

def pc(request):
    form = None  # Inicializa la variable form

    if request.method == 'POST':
        if 'editar' in request.POST:
            computador_id = request.POST.get('computador_id')
            computador = get_object_or_404(Computadores, id_computador=computador_id)
            form = ComputadoresForm(request.POST, instance=computador)
            if form.is_valid():
                form.save()
                return redirect('computador')
        elif 'eliminar' in request.POST:
            computador_id = request.POST.get('computador_id')
            computador = get_object_or_404(Computadores, id_computador=computador_id)
            computador.delete()
            return redirect('computador')
        elif 'crear' in request.POST:
            form = ComputadoresForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('computador')
    else:
        computador_id = request.GET.get('computador_id')
        if computador_id:
            sala = get_object_or_404(Computadores, id_computador=computador_id)
            form = ComputadoresForm(instance=computador)
        else:
            form = ComputadoresForm()
    
    computadores = Computadores.objects.all()
    salas = Sala.objects.all()  # Obtener todas las salas
    return render(request, 'pc.html', {'computadores': computadores, 'form': form, 'edit': computador_id is not None, 'salas': salas})