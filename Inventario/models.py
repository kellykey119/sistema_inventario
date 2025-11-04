from django.db import models

# Create your models here
class Equipo(models.Model):
    ESTADOS = [
        ('Operativo', 'Operativo'),
        ('En reparación', 'En reparación'),
        ('Dado de baja', 'Dado de baja'),
    ]

    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    numero_serie = models.CharField(max_length=100)
    año_compra = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADOS)

    def __str__(self):
        return f"{self.marca} - {self.modelo}"