# views/urls.py

from django.shortcuts import render


# Create your views here.
def adminusers(request):
    return render(request, "admin-users.html")
