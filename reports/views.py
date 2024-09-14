from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Reportes
from .forms import ReporteForm
from room.models import Computadores

def reports(request):
    reportes_list = Reportes.objects.all()
    paginator = Paginator(reportes_list, 10)  # Mostrar 10 reportes por página
    page = request.GET.get('page')
    try:
        reportes = paginator.page(page)
    except PageNotAnInteger:
        reportes = paginator.page(1)
    except EmptyPage:
        reportes = paginator.page(paginator.num_pages)
    return render(request, "reports.html", {'reportes': reportes})

def new_report(request):
    computadores = Computadores.objects.all()
    if request.method == 'POST':
        form = ReporteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reports')
    else:
        form = ReporteForm()
    return render(request, "new_reports.html", {'form': form, 'computadores': computadores})

def edit_report(request, id_reportes):
    reporte = get_object_or_404(Reportes, id_reportes=id_reportes)
    computadores = Computadores.objects.all()
    if request.method == 'POST':
        form = ReporteForm(request.POST, instance=reporte)
        if form.is_valid():
            form.save()
            return redirect('reports')
    else:
        form = ReporteForm(instance=reporte)
    return render(request, 'new_reports.html', {'form': form, 'computadores': computadores})

def delete_report(request, id_reportes):
    reporte = get_object_or_404(Reportes, id_reportes=id_reportes)
    reporte.delete()
    return redirect('reports')
