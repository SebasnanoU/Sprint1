from django.db import models

class Cliente(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre_completo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return str(self.cedula) + " " + self.nombre_completo