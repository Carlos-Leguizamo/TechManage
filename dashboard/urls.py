# dashboard/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path("dashboard/", views.dashboard, name='dashboard'),
    path("sala/", views.sala, name='sala'),


]
