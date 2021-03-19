from django.db import models

class Vendedor(models.Model):
    tienda = models.TextField()

    def __str__(self):
        return self.tienda

class Post(models.Model):
    nombre = models.CharField(max_length=100)
    vendedor  = models.ForeignKey(
        Vendedor,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    descripcion = models.TextField()
    imagen = models.TextField(default='')
    precio = models.TextField(default='')


    def __str__(self):
        return self.nombre