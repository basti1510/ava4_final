from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Reserva(models.Model):
    ESTADOS_RESERVA = (
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    )

    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    cantidad_personas = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(15)]
    )
    estado = models.CharField(max_length=20, choices=ESTADOS_RESERVA)
    observacion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} - Reserva {self.id}"
