# Generated by Django 5.1 on 2024-09-19 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pqrs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pqrs',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('resuelto', 'Resuelto')], default='pendiente', max_length=20),
        ),
        migrations.AlterField(
            model_name='pqrs',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
