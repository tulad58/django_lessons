from django.db import models
from datetime import datetime

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250, blank=True)
    # measurements = models.ForeignKey('Measurement', related_name='measurements', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, related_name='sensor', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"id measure: {self.id}"
