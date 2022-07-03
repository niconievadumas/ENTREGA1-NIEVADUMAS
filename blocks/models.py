from django.db import models

# Create your models here.

class Blocks(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    fecha_registro = models.DateField(null=True)
    
    def __str__(self):
        return f"{self.titulo} - {self.autor} "
