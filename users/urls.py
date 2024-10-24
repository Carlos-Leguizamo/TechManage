from django.urls import path
from . import views

urlpatterns = [
    # URL para la seccion de adminitracion de usuario
    path("admin-user/", views.adminusers, name='adminusers'),
    # URL para la eliminacion del usuario y pasamos el token por la URL
    path('delete_user/<str:token_verification>/', views.delete_user, name='delete_user'),
    # URL para la confirmacion de eliminacion del usuario y pasamos el token por la URL
    path('confirm_delete_user/<str:token_verification>/', views.confirm_delete_user, name='confirm_delete_user'),


    path('profile/update/<str:token_verification>/', views.update_user, name='update_user'),
    path('no_autorizado/', views.no_auth, name='no_auth'),
     


]
