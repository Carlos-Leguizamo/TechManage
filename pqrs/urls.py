# urls/pqrs


from django.urls import path
from . import views

urlpatterns = [

    # Definir ruta para mostrar la vista de PQRS
       path("pqrs/", views.view_pqrs, name='view-pqrs'),
       path("pending-pqrs/", views.pending_pqrs, name='view-pending-pqrs'), # Vista de PQRS pendientes del usuario
]