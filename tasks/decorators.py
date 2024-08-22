from django.shortcuts import redirect

def validacion_requerida(view_func):
    def _wrapped_view(request, *args, **kwargs):
        # Redirigir a la vista de validación si no ha sido validado
        if not request.session.get('validado', False):
            return redirect('send_token')
        
        # Si ya está validado, permitir el acceso a la vista
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def token_requerido(view_func):
    def _wrapped_view(request, *args, **kwargs):
        # Verifica si el usuario ha pasado por la vista de envío de token
        if not request.session.get('token_verificado', False):
            return redirect('send_token')
        return view_func(request, *args, **kwargs)
    return _wrapped_view