from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    # Otros campos que puedan ser relevantes para tu aplicación

    def __str__(self):
        return self.nombre
