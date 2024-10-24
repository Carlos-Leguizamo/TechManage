from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from room.models import Sala, Computadores
from reports.models import Reportes

@login_required
def dashboard(request):
    total_salas = Sala.objects.count()
    total_computadores = Computadores.objects.count()
    total_reportes = Reportes.objects.count()
    total_computadores_dañados = Computadores.objects.filter(estado="dado de baja").count()
    total_computadores_operativos = Computadores.objects.filter(estado="operativo").count()
    total_computadores_en_reparacion = Computadores.objects.filter(estado="en reparación").count()
        
    
    
    context = {
        "total_salas": total_salas,
        "total_computadores": total_computadores,
        "total_reportes": total_reportes,
        "total_computadores_dañados": total_computadores_dañados,
        "total_computadores_operativos": total_computadores_operativos,
        "total_computadores_en_reparacion": total_computadores_en_reparacion,

    }

    return render(request, "dashboard.html", context)


@login_required
def buscador(request):
    busqueda = request.GET.get("buscar")
    salas = Sala.objects.all()
    computadores = Computadores.objects.all()

    if busqueda:
        salas = salas.filter(
            Q(nombre_sala__icontains=busqueda) | Q(ubicacion__icontains=busqueda)
        ).distinct()
        computadores = computadores.filter(
            Q(tipo__icontains=busqueda)
            | Q(marca__icontains=busqueda)
            | Q(modelo__icontains=busqueda)
            | Q(estado__icontains=busqueda)
        ).distinct()

    context = {
        "salas": salas,
        "computadores": computadores,
        "busqueda": busqueda,
    }

    return render(request, "buscador.html", context)
