from django.db import models
from django.contrib.auth.models import User

class PQRS(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En proceso'),
        ('resuelto', 'Resuelto'),
    ]

    id_pqrs = models.AutoField(primary_key=True)
    fecha_creacion = models.DateTimeField()
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'PQRS'

class Reportes(models.Model):
    id_reportes = models.AutoField(primary_key=True)
    nombre_reporte = models.CharField(max_length=45)
    fecha = models.DateTimeField()
    descripcion = models.TextField()
    id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Reportes'




