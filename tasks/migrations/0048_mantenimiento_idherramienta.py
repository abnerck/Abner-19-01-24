# Generated by Django 4.2.5 on 2023-10-10 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0047_mantenimiento_fechamantenimineto'),
    ]

    operations = [
        migrations.AddField(
            model_name='mantenimiento',
            name='idHerramienta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.herramienta'),
        ),
    ]