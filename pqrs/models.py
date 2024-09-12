from django.db import models
from django.contrib.auth.models import User

class PQRS(models.Model):
    # Opciones para el tipo de solicitud
    TIPO_CHOICES = [
        ('peticion', 'Petición'),
        ('queja', 'Queja'),
        ('reclamo', 'Reclamo'),
        ('sugerencia', 'Sugerencia'),
    ]

    # Opciones para el estado de la solicitud
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En proceso'),
        ('resuelto', 'Resuelto'),
    ]

    id_pqrs = models.AutoField(primary_key=True)
    fecha_creacion = models.DateTimeField()
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='peticion') # Nuevo campo para el tipo de solicitud
    id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'PQRS'