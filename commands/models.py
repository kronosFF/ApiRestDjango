from django.db import models

# Create your models here.

class Command(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre Comando')
    description = models.TextField(verbose_name='Descripción')
    parameters = models.TextField(verbose_name='Parámetros')
    image = models.ImageField(upload_to='img', null=True)
    
    class Meta:
        verbose_name = 'Comando'
        verbose_name_plural = 'Productos'
        ordering = ['name']
    
    def __str__(self) -> str:
        return self.name 