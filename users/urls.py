# users/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path("admin-user/", views.adminusers, name='adminusers'),
   
    
]
