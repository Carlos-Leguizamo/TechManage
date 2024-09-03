from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Sala
from .forms import SalaForm  
from .models import Computadores
from .forms import ComputadorForm

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

#@login_required
def pc(request):
    pc_id = None  # Asegúrate de que `pc_id` esté definida al inicio

    if request.method == 'POST':
        if 'editar' in request.POST:
            pc_id = request.POST.get('pc_id')
            computador = get_object_or_404(Computadores, id_computador=pc_id)
            form = ComputadorForm(request.POST, instance=computador)
            if form.is_valid():
                form.save()
                return redirect('pc')
        elif 'eliminar' in request.POST:
            pc_id = request.POST.get('pc_id')
            computador = get_object_or_404(Computadores, id_computador=pc_id)
            computador.delete()
            return redirect('pc')
        elif 'crear' in request.POST:
            form = ComputadorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('pc')
    else:
        form = ComputadorForm()

    computadores = Computadores.objects.all()
    salas = Sala.objects.all() 
    return render(request, 'pc.html', {'computadores': computadores, 'salas': salas, 'form': form, 'edit': pc_id is not None})