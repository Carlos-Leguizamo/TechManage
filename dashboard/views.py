from django.shortcuts import render
from django.contrib.auth.decorators import login_required #Seguridad de las rutas y no permitir acceso mediantre ellas si no esta logueado

#Seguridad de la ruta  
@login_required
def dashboard(request):
    return render(request, "dashboard.html")



