
# Generated by Django 5.1 on 2024-09-12 13:08

from django.db import migrations, models



class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_sala_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computadores',
            name='id_sala',
        ),
        migrations.RemoveField(
            model_name='perifericos',
            name='id_computador',
        ),
        migrations.RemoveField(
            model_name='mantenimiento',
            name='id_computador',
        ),
        migrations.RemoveField(
            model_name='mantenimiento',
            name='id',
        ),

        migrations.RemoveField(
            model_name='reportes',
            name='id',

        migrations.AddField(
            model_name='pqrs',
            name='tipo',
            field=models.CharField(choices=[('peticion', 'Petición'), ('queja', 'Queja'), ('reclamo', 'Reclamo'), ('sugerencia', 'Sugerencia')], default='peticion', max_length=20),

        ),
        migrations.DeleteModel(
            name='Sala',
        ),
        migrations.DeleteModel(
            name='Perifericos',
        ),
        migrations.DeleteModel(
            name='Computadores',
        ),
        migrations.DeleteModel(
            name='Mantenimiento',
        ),

        migrations.DeleteModel(
            name='Reportes',
        ),


    ]
