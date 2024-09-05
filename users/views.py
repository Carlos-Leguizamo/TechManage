from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from django.contrib.auth.models import User
from .forms import CustomUserChangeForm 


# Logica para mostar los usuarios en la tabal y retornar la vista de la tabla de administracion de usuarios
@login_required
def adminusers(request):
    # User.objects.all traigo todo los usuarios de la BD
    users_list = User.objects.all()
    paginator = Paginator(users_list, 5)  # Muestra 10 usuarios por página

    page_number = request.GET.get("page")
    users = paginator.get_page(page_number)

    return render(request, "admin-users.html", {"users": users})

# Logica para eliminar usuario
@login_required
# @user_passes_test(lambda u: u.is_superuser)
def confirm_delete_user(request, token_verification):
    # Obtener el perfil del usuario a través del token de verificación
    user_profile = get_object_or_404(UserProfile, token_verification=token_verification)
    user_to_delete = user_profile.user

    if request.method == "POST":
        if user_to_delete == request.user:
            # messages.error(request, "No puedes eliminar tu propia cuenta.")
            return redirect("adminusers")

        # Eliminar usuario y su perfil
        user_to_delete.delete()
        user_profile.delete()  # Eliminar también el perfil asociado
        messages.success(request, f"Usuario {user_to_delete.username} eliminado con éxito.")
        return redirect("adminusers")

    # Renderizar la plantilla de confirmación
    return render(request, "confirm_delete_user.html", {"user_to_delete": user_to_delete})

# Logica de Confirmacion para eliminar el usuario 
@login_required
def delete_user(request, token_verification):
    # Verificar si el token es válido
    user_profile = get_object_or_404(UserProfile, token_verification=token_verification)
    user_to_delete = user_profile.user

    # Redirigir a la vista de confirmación de eliminación de usuario
    return redirect("confirm_delete_user", token_verification=token_verification)


@login_required
def update_user(request, token_verification):
    user_profile = get_object_or_404(UserProfile, token_verification=token_verification)
    user_to_update = user_profile.user

    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user_to_update)
        if form.is_valid():
            form.save()
            messages.success(request, f'La informacion del usuario {user_to_update.username} ha sido actuliazada correctamente')
            # Redirige a la vista de la tabla de administracion de usuarios
            return redirect('adminusers')
    else:
        form = CustomUserChangeForm(instance=user_to_update)

    return render(request, 'confirm_update_user.html', {'form': form, 'user': user_to_update})

