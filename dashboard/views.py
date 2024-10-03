from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from room.models import Sala
from room.forms import SalaForm  


@login_required  
def dashboard(request):
    return render(request, "dashboard.html")
