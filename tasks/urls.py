from django.contrib import admin
from django.urls import path, include
from tasks import views


urlpatterns = [
    path("", views.home , name='home'),
    path("register/", views.register, name='register'),
    path("logout/", views.signout, name='logout'),
    path("signin/", views.signin, name='sigin'),
]