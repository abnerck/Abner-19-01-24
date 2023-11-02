# Generated by Django 4.2.5 on 2023-10-04 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0018_incidenteslaborales'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncidenteLaboral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horaIncidente', models.TimeField(blank=True, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('reportadopor', models.IntegerField(blank=True, null=True)),
                ('tipoIncidente', models.CharField(blank=True, max_length=100, null=True)),
                ('accionesCorrectivas', models.CharField(blank=True, max_length=100, null=True)),
                ('comentarios', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='IncidentesLaborales',
        ),
    ]
