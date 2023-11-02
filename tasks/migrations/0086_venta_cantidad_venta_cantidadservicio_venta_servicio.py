# Generated by Django 4.2.5 on 2023-11-01 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0085_remove_venta_idorden_venta_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='cantidad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='cantidadservicio',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='servicio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.servicio'),
        ),
    ]
