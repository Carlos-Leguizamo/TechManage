from django.contrib import admin
from django.urls import path, include
from tasks import views
from .views import send_verification_email, verify_token_view


urlpatterns = [
    path("", views.home , name='home'),
    path("register/", views.register, name='register'),
    path("logout/", views.signout, name='logout'),
    path("signin/", views.signin, name='sigin'),
    path('send-code/', send_verification_email, name='send_code'),
    path('verify-token/', verify_token_view, name='verify_token'),
]