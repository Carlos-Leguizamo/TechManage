from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from django.contrib.auth.models import User


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
# @user_passes_test(lambda u: u.is_superuser)
def confirm_delete_user(request, token_verification):
    user_profile = get_object_or_404(UserProfile, token_verification=token_verification)
    user = user_profile.user

    if request.method == "POST":
        print("POST request received")  # Depuración
        print(f"Deleting user: {user.username}")  # Depuración

        if user == request.user:
            messages.error(request, "No puedes eliminar tu propia cuenta.")
            return redirect("adminusers")

        user.delete()
        user_profile.delete()  # Asegúrate de eliminar el perfil si es necesario
        messages.success(request, "Usuario eliminado con éxito.")
        return redirect("adminusers")

    return render(request, "confirm_delete_user.html", {"user": user})



def delete_user(request, token_verification):
    # Verifica si el token es válido
    user_profile = get_object_or_404(UserProfile, token_verification=token_verification)
    user = user_profile.user

    # Redirige a la vista de confirmación con el token
    return redirect("confirm_delete_user", token_verification=token_verification)