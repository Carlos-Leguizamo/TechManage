from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Sala
from .forms import SalaForm  

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
