
from django.db import models

class Car(models.Model):
    title = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()
    description = models.TextField()

    def __str__(self):
        return f"{self.title} ({self.year})"
