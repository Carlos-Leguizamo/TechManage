from django.db import models
from django.contrib.auth.models import User

class PQRS(models.Model):
    TIPO_CHOICES = [
        ('peticion', 'Petición'),
        ('queja', 'Queja'),
        ('reclamo', 'Reclamo'),
        ('sugerencia', 'Sugerencia'),
    ]

    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('resuelto', 'Resuelto'),
    ]

    id_pqrs = models.AutoField(primary_key=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Se establece la fecha automáticamente
    descripcion = models.TextField()
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='pendiente'  # Valor por defecto
    )
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='peticion')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 

    class Meta:
        db_table = 'PQRS'
