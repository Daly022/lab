from django.db import models

# Create your models here.

class Producto(models.Model):
    product_name = models.CharField(max_length=200)
    product_descrip = models.CharField(max_length=1000)
    product_category = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='post/%y/%m/%d', default='post/pic01.jpg')
    numero = models.IntegerField(null=True)

    def __str__(self):
        return self.product_name

class Encuesta(models.Model):
    class Suit(models.TextChoices):
        MUY_MALO = 'Muy Malo', ('MUY MALO')
        MALO = 'Malo', ('MALO')
        REGULAR = 'Regular', ('REGULAR')
        BUENO = 'Bueno', ('BUENO')
        EXCELENTE = 'Excelente', ('EXCELENTE')
        __empty__ = ('Seleccione')

    class tamano(models.TextChoices):
        MUY_MALO = 'Muy barato', ('MUY BARATO')
        MALO = 'Economico', ('ECONOMICO')
        REGULAR = 'Aceptable', ('ACEPTABLE')
        BUENO = 'Costoso', ('COSTOSO')
        EXCELENTE = 'Muy caro', ('MUY CARO')
        __empty__ = ('Seleccione')
    product_name = models.ForeignKey(Producto,on_delete= models.CASCADE)
    encuesta_contenido = models.TextField(max_length=10000)
    product_lugarCompra = models.CharField(max_length=100)
    product_calificacion = models.CharField(choices=Suit.choices,max_length=100)
    product_precio = models.PositiveIntegerField(default=0)
    product_precioTamano = models.CharField(choices=tamano.choices,max_length=100)
    product_calidad = models.CharField(choices=Suit.choices,max_length=100)
