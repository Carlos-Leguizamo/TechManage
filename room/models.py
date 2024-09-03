from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sala(models.Model):
    id_sala = models.AutoField(primary_key=True)
    nombre_sala = models.CharField(max_length=45)
    descripcion = models.TextField()
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length=45)
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Establece automáticamente la fecha de creación
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)  # Valor por defecto para 'estado'
    inventario_cantidad = models.IntegerField()

    class Meta:
        db_table = 'Sala'

class Computadores(models.Model):
    ESTADO_CHOICES = [
        ('operativo', 'Operativo'),
        ('en reparación', 'En reparación'),
        ('dado de baja', 'Dado de baja'),
    ]

    id_computador = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=45)
    marca = models.CharField(max_length=45)
    modelo = models.CharField(max_length=45)
    numero_serie = models.CharField(max_length=45)
    fecha_adquisicion = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    id_sala = models.ForeignKey(Sala, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Computadores'

class Perifericos(models.Model):
    TIPO_CHOICES = [
        ('mouse', 'Mouse'),
        ('teclado', 'Teclado'),
        ('monitor', 'Monitor'),
        ('camara', 'Cámara'),
    ]
    
    ESTADO_CHOICES = [
        ('operativo', 'Operativo'),
        ('en reparación', 'En reparación'),
        ('dado de baja', 'Dado de baja'),
    ]

    id_perifericos = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    marca = models.CharField(max_length=45)
    modelo = models.CharField(max_length=45)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    descripcion = models.TextField()
    id_computador = models.ForeignKey(Computadores, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Perifericos'

class Mantenimiento(models.Model):
    TIPO_MANTENIMIENTO_CHOICES = [
        ('preventivo', 'Preventivo'),
        ('correctivo', 'Correctivo'),
    ]

    id_mantenimiento = models.AutoField(primary_key=True)
    id_computador = models.ForeignKey(Computadores, on_delete=models.CASCADE)
    fecha_programada = models.DateTimeField()
    fecha_realizacion = models.DateTimeField()
    tipo_mantenimiento = models.CharField(max_length=20, choices=TIPO_MANTENIMIENTO_CHOICES)
    descripcion_mantenimiento = models.TextField()
    tecnico_responsable = models.CharField(max_length=45)
    proximo_mantenimiento = models.DateTimeField()
    id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Mantenimiento'