from django.db import models

# Create your models here.
class predio(models.Model):
    tipos_predios = (
         ('U', 'urbanos'),
        ('R', 'rural')
    )
    id = models.AutoField(primary_key = True)
    cedula_catastral = models.CharField(max_length=19, blank=False, null=False)
    direccion = models.CharField(max_length=200, blank=False)
    tipo = models.CharField(max_length=1, blank=False, null=False, choices=tipos_predios, default=tipos_predios[1][1])
    identificacion = models.CharField(max_length=10, blank=False, null=False, default="00000000")

    class Meta:

        verbose_name = 'predio'
        verbose_name_plural = "predios"


