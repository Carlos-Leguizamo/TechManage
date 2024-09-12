# urls/pqrs


from django.urls import path
from . import views

urlpatterns = [

    # Definir ruta para mostrar la vista de PQRS
       path("pqrs/", views.view_pqrs, name='view-pqrs'),
]