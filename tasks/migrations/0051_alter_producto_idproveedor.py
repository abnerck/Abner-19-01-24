# Generated by Django 4.2.5 on 2023-10-10 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0050_producto_idproveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='idProveedor',
            field=models.ForeignKey(blank=True, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.proveedor'),
        ),
    ]