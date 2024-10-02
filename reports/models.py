from django.db import models
from django.utils import timezone
from room.models import Computadores

class Reportes(models.Model):
    id_reportes = models.AutoField(primary_key=True)
    nombre_reporte = models.CharField(max_length=45)
    fecha = models.DateTimeField(default=timezone.now) 
    descripcion = models.TextField()
    id_computador = models.ForeignKey(Computadores, on_delete=models.CASCADE, db_column='id_computador')
    tecnico_responsable = models.CharField(max_length=45)

    class Meta:
        db_table = 'Reportes'
