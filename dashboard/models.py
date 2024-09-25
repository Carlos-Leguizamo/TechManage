from django.db import models
from django.contrib.auth.models import User

class Reportes(models.Model):
    id_reportes = models.AutoField(primary_key=True)
    nombre_reporte = models.CharField(max_length=45)
    fecha = models.DateTimeField()
    descripcion = models.TextField()
    id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table='Reportes'