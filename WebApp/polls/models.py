from django.db import models

# Create your models here.
class Producto(models.Model):
    product_name = models.CharField(max_length=200, primary_key=True)
    product_descrip = models.CharField(max_length=1000)
    product_category = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='post/%y/%m/%d', default='post/pic01.jpg')

class Encuesta(models.Model):
    product_name = models.ForeignKey(Producto, on_delete=models.CASCADE)
    encuesta_contenido = models.CharField(max_length=5000)
    product_lugarCompra = models.CharField(max_length=100)
    product_calificacion = models.IntegerField(default=0)
    product_precio = models.FloatField(default=0)
    product_precioTamano = models.IntegerField(default=0)
    product_tiempoUso = models.IntegerField(default=0)
    product_calidad = models.IntegerField(default=0)
