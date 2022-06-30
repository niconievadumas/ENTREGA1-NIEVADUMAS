from django.db import models

# Create your models here.

class Blocks(models.Model):
    titulo = models.CharField(max_length=30)
    contenido = models.CharField(max_length=30)
    fecha = models.DateField(null=True)
