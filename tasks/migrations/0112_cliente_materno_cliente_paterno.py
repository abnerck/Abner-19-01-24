# Generated by Django 4.2.5 on 2024-01-27 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0111_remove_cliente_apellidom_remove_cliente_apellidop'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='materno',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='paterno',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
