from django.db import models
from django.contrib.auth.models import User
from room.models import Computadores
from django.utils import timezone

class Reportes(models.Model):
    id_reportes = models.AutoField(primary_key=True)
    nombre_reporte = models.CharField(max_length=45)
    fecha = models.DateTimeField(default=timezone.now) 
    descripcion = models.TextField()
    id_computador = models.ForeignKey(Computadores, on_delete=models.CASCADE, db_column='id_computador')
    tecnico_responsable = models.CharField(max_length=45)

    class Meta:
        db_table='Reportes'
 