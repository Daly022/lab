from django import forms
from .models import Producto
from .models import Encuesta

class formularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('product_name','product_descrip','product_category','product_image')

class formularioEncuesta(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = ('product_name', 'encuesta_contenido','product_lugarCompra','product_calificacion','product_precio','product_precioTamano','product_calidad')