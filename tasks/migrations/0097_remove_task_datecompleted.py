# Generated by Django 4.2.5 on 2023-12-12 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0096_alter_herramienta_valor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='datecompleted',
        ),
    ]
