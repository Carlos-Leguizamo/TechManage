# dashboard/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path("sala/", views.sala, name='sala'),


]
