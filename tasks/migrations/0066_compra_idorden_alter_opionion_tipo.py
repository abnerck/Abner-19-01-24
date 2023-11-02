# Generated by Django 4.2.5 on 2023-10-11 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0065_alter_orden_totalorden'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='idOrden',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.orden'),
        ),
        migrations.AlterField(
            model_name='opionion',
            name='tipo',
            field=models.CharField(blank=True, choices=[('Queja', 'Queja'), ('Opinion', 'Opinion'), ('Sugerencia', 'Sugerencia')], max_length=100, null=True),
        ),
    ]
