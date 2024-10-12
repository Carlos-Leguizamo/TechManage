from django.db import models
from django.utils import timezone
from room.models import Computadores

class Reportes(models.Model):
    TIPO_MANTENIMIENTO_CHOICES = [
        ('Preventivo', 'Preventivo'),
        ('Correctivo', 'Correctivo'),
    ]

    id_reportes = models.AutoField(primary_key=True)
    nombre_reporte = models.CharField(max_length=45)
    fecha = models.DateTimeField(default=timezone.now) 
    descripcion = models.TextField()
    id_computador = models.ForeignKey(Computadores, on_delete=models.CASCADE, db_column='id_computador')
    tecnico_responsable = models.CharField(max_length=45)
    tipo_mantenimiento = models.CharField(max_length=11, choices=TIPO_MANTENIMIENTO_CHOICES, default='Preventivo')

    class Meta:
        db_table='Reportes'

