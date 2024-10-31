# dashboard/urls.py

from django.urls import path
from . import views
from .views import buscador


urlpatterns = [
    path("dashboard/", views.dashboard, name='dashboard'),
    path("buscador/", views.buscador, name='buscador'), 


]
