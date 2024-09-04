# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("admin-user/", views.adminusers, name='adminusers'),
 # urls.py
    path('delete_user/<str:token_verification>/', views.delete_user, name='delete_user'),
    path('confirm_delete_user/<str:token_verification>/', views.confirm_delete_user, name='confirm_delete_user'),

]
