# Generated by Django 4.2.5 on 2024-01-29 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0113_alter_cliente_materno_alter_cliente_paterno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentelaboral',
            name='horaIncidente',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='opionion',
            name='tipo',
            field=models.CharField(blank=True, choices=[('Queja', 'Queja'), (' ', 'Opinion'), ('Sugerencia', 'Sugerencia')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='telefono',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
