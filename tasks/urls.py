from django.contrib import admin
from django.urls import path, include
from tasks import views



urlpatterns = [
    path("", views.home , name='home'),
    path("register/", views.register, name='register'),
    path("logout/", views.signout, name='logout'),
    path("signin/", views.signin, name='sigin'),
    path('send-token/', views.send_verification_email, name='send_token'),
    path('verify-token/', views.verify_token_view, name='verify_token'),
]