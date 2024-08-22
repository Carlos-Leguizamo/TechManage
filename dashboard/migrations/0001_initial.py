# Generated by Django 5.1 on 2024-08-22 19:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Computadores',
            fields=[
                ('id_computador', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=45)),
                ('marca', models.CharField(max_length=45)),
                ('modelo', models.CharField(max_length=45)),
                ('numero_serie', models.CharField(max_length=45)),
                ('fecha_adquisicion', models.DateTimeField()),
                ('estado', models.CharField(choices=[('operativo', 'Operativo'), ('en reparación', 'En reparación'), ('dado de baja', 'Dado de baja')], max_length=20)),
            ],
            options={
                'db_table': 'Computadores',
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id_sala', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_sala', models.CharField(max_length=45)),
                ('descripcion', models.TextField()),
                ('capacidad', models.IntegerField()),
                ('ubicacion', models.CharField(max_length=45)),
                ('fecha_creacion', models.DateTimeField()),
                ('fecha_actualizacion', models.DateTimeField()),
                ('estado', models.BooleanField()),
                ('inventario_cantidad', models.IntegerField()),
            ],
            options={
                'db_table': 'Sala',
            },
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id_mantenimiento', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_programada', models.DateTimeField()),
                ('fecha_realizacion', models.DateTimeField()),
                ('tipo_mantenimiento', models.CharField(choices=[('preventivo', 'Preventivo'), ('correctivo', 'Correctivo')], max_length=20)),
                ('descripcion_mantenimiento', models.TextField()),
                ('tecnico_responsable', models.CharField(max_length=45)),
                ('proximo_mantenimiento', models.DateTimeField()),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_computador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.computadores')),
            ],
            options={
                'db_table': 'Mantenimiento',
            },
        ),
        migrations.CreateModel(
            name='Perifericos',
            fields=[
                ('id_perifericos', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[('mouse', 'Mouse'), ('teclado', 'Teclado'), ('monitor', 'Monitor'), ('camara', 'Cámara')], max_length=20)),
                ('marca', models.CharField(max_length=45)),
                ('modelo', models.CharField(max_length=45)),
                ('estado', models.CharField(choices=[('operativo', 'Operativo'), ('en reparación', 'En reparación'), ('dado de baja', 'Dado de baja')], max_length=20)),
                ('descripcion', models.TextField()),
                ('id_computador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.computadores')),
            ],
            options={
                'db_table': 'Perifericos',
            },
        ),
        migrations.CreateModel(
            name='PQRS',
            fields=[
                ('id_pqrs', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField()),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En proceso'), ('resuelto', 'Resuelto')], max_length=20)),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'PQRS',
            },
        ),
        migrations.CreateModel(
            name='Reportes',
            fields=[
                ('id_reportes', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_reporte', models.CharField(max_length=45)),
                ('fecha', models.DateTimeField()),
                ('descripcion', models.TextField()),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Reportes',
            },
        ),
        migrations.AddField(
            model_name='computadores',
            name='id_sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.sala'),
        ),
    ]
