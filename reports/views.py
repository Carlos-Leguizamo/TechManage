from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Reportes
from .forms import ReporteForm
from room.models import Computadores, Sala
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test

@user_passes_test(lambda u: u.is_superuser, login_url='no_auth')
@login_required
def reports(request):
    reportes_list = Reportes.objects.all()
    paginator = Paginator(reportes_list, 5)  # Mostrar 5 reportes por página
    page = request.GET.get('page')
    try:
        reportes = paginator.page(page)
    except PageNotAnInteger:
        reportes = paginator.page(1)
    except EmptyPage:
        reportes = paginator.page(paginator.num_pages)
    return render(request, "reports.html", {'reportes': reportes})

@user_passes_test(lambda u: u.is_superuser, login_url='no_auth')
@login_required
def delete_report(request, id_reportes):
    reporte = get_object_or_404(Reportes, id_reportes=id_reportes)
    reporte.delete()
    return redirect('reports')

@user_passes_test(lambda u: u.is_superuser, login_url='no_auth')
@login_required
def new_report(request):
    computadores = Computadores.objects.all()
    if request.method == 'POST':
        form = ReporteForm(request.POST)
        if form.is_valid():
            reporte = form.save(commit=False)
            reporte.fecha = timezone.now()  # Usa la hora actual en la zona horaria configurada
            reporte.save()
            return redirect('reports')
    else:
        form = ReporteForm()
    return render(request, "new_reports.html", {'form': form, 'computadores': computadores})

# View para convertir reporte a PDF
@user_passes_test(lambda u: u.is_superuser, login_url='no_auth')
@login_required
def generate_pdf_view(request, id_reportes):
    reporte = get_object_or_404(Reportes, id_reportes=id_reportes)
    computador = get_object_or_404(Computadores, id_computador=reporte.id_computador.id_computador)
    sala = get_object_or_404(Sala, id_sala=computador.id_sala.id_sala)  # Obtén la sala del computador

    template_path = 'pdf_template.html'
    context = {
        'reporte': reporte,
        'computador': computador,  # Incluye los datos del computador
        'sala': sala  # Incluye la sala en el contexto
    }

    # Cargar plantilla y contexto en el PDF
    template = get_template(template_path)
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="reporte.pdf"'

    # Generar PDF usando pisa
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF: %s' % pisa_status.err)

    return response