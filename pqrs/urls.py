# urls/pqrs


from django.urls import path
from . import views

urlpatterns = [

    # Definir ruta para mostrar la vista de PQRS
       path("pqrs/", views.view_pqrs, name='view-pqrs'),
       path("pending-pqrs/", views.pending_pqrs, name='view-pending-pqrs'), # Vista de PQRS pendientes del usuario
       path("admin-pqrs/", views.admin_pqrs, name='view-admin-pqrs'),
       path('confirm-delete-pqrs/<int:id>/', views.confirm_delete_pqrs, name='confirm_delete_pqrs'),

       
       path('check-pqrs/<int:id>/', views.check_pqrs, name='check_pqrs'),


]