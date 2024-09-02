# users/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path("admin-user/", views.adminusers, name='adminusers'),
    # path('user_management/', views.user_management, name='user_management'),  # Añade esta línea
    path('delete_user/<int:user_id>/', views.confirm_delete_user, name='confirm_delete_user'),
#  path('confirm-delete/', views.confirm_delete_user, name='confirm_delete_user'),
   
    
]
