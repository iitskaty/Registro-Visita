from django.db import models

# Create your models here.
class Visita(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    fecha_de_visita = models.DateField()
    motivo = models.TextField()

    def __str__(self):
        return f"{self.nombre} - {self.rut}"