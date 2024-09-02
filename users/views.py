from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 

@login_required
def adminusers(request):
    # User.objects.all traigo todo los usuarios de la BD
    users_list = User.objects.all()
    paginator = Paginator(users_list, 5)  # Muestra 10 usuarios por página

    page_number = request.GET.get('page')
    users = paginator.get_page(page_number)

    return render(request, 'admin-users.html', {'users': users})
