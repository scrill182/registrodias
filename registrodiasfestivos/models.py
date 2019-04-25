

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Registro(models.Model):

    no_cobro=models.IntegerField( null=False)
    nombre= models.CharField(max_length=200)
    horario = models.CharField(max_length=200)
    fecha_creacion= models.DateTimeField( default=timezone.now())
    diasFestivos = models.DateField(null=False)
    objects = models.Manager()

    def creacion(self):
        self.fecha_creacion = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre





