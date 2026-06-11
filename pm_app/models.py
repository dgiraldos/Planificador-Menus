from django.db import models

# Create your models here.

class Comida(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Planificacion(models.Model):
    DIAS_SEMANA = [
        ("lunes", "Lunes"),
        ("martes", "Martes"),
        ("miercoles", "Miércoles"),
        ("jueves", "Jueves"),
        ("viernes", "Viernes"),
        ("sabado", "Sábado"),
        ("domingo", "Domingo"),
    ]

    TIPOS_COMIDA = [
        ("desayuno", "Desayuno"),
        ("comida", "Comida"),
        ("cena", "Cena"),
    ]

    dia = models.CharField(max_length=10, choices=DIAS_SEMANA)
    tipo_comida = models.CharField(max_length=10, choices=TIPOS_COMIDA)
    comida = models.ForeignKey(
        Comida,
        on_delete=models.CASCADE,
        related_name="planificaciones"
    )

    class Meta:
        verbose_name = "planificación"
        verbose_name_plural = "planificaciones"
        unique_together = ("dia", "tipo_comida")

    def __str__(self):
        return f"{self.get_dia_display()} - {self.get_tipo_comida_display()} - {self.comida.nombre}"