# Generated by Django 5.0.6 on 2024-06-13 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_precio_blame_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='administrador',
            options={'ordering': ('-creado', 'apellidos', 'nombre'), 'verbose_name_plural': 'Administradores'},
        ),
        migrations.AlterModelOptions(
            name='profesor',
            options={'ordering': ('-creado', 'apellidos', 'nombre'), 'verbose_name_plural': 'Profesores'},
        ),
    ]
