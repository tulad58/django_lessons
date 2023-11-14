# Generated by Django 4.2.4 on 2023-09-26 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0006_remove_sensor_measurements'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='sensor',
        ),
        migrations.AddField(
            model_name='sensor',
            name='measurements',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.measurement'),
        ),
    ]
