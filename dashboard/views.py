from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from room.models import Sala, Computadores

@login_required  
def dashboard(request):
    return render(request, "dashboard.html")

@login_required
def buscador(request):
    busqueda = request.GET.get("buscar")
    salas = Sala.objects.all()
    computadores = Computadores.objects.all()

    if busqueda:
        salas = salas.filter(
            Q(nombre_sala__icontains=busqueda) |
            Q(ubicacion__icontains=busqueda)
        ).distinct()
        computadores = computadores.filter(
            Q(tipo__icontains=busqueda) |
            Q(marca__icontains=busqueda) |
            Q(modelo__icontains=busqueda) |
            Q(estado__icontains=busqueda)
        ).distinct()

    context = {
        'salas': salas,
        'computadores': computadores,
        'busqueda': busqueda,
    }

    return render(request, 'buscador.html', context)
