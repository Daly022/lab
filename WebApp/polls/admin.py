from django.contrib import admin

# Register your models here.
from .models import Encuesta
from .models import Producto

admin.site.register(Encuesta)
admin.site.register(Producto)
