from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404


# Logica para mostar los usuarios en la tabal y retonrar la vista de la tabla de administracion de usuarios
@login_required
def adminusers(request):
    # User.objects.all traigo todo los usuarios de la BD
    users_list = User.objects.all()
    paginator = Paginator(users_list, 5)  # Muestra 10 usuarios por página

    page_number = request.GET.get("page")
    users = paginator.get_page(page_number)

    return render(request, "admin-users.html", {"users": users})


@login_required
def confirm_delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        user.delete()
        messages.success(request, "Usuario eliminado con éxito.")
        return redirect(
            "adminusers"
        )  # Redirige a la página de administración de usuarios

    return render(request, "confirm_delete_user.html", {"user": user})
