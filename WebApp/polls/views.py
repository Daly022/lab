# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from .models import Encuesta,Producto
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import formularioProducto,formularioEncuesta

def listreview(request):
    reviews = Encuesta.objects.all().order_by('product_calificacion')
    context = {
        'reviews': reviews
    }
    return render(request, 'inicio.html', context)

def resepro(request, product):
    products = Producto.objects.filter(product_name=product)
    for i in products:
        reviews = Encuesta.objects.filter(product_name=i.id)
    if len(reviews)>0 :
        context = {
            'products': products,
            'reviews': reviews
        }
    else:
        context = {
            'products': products,
            'reviews': 'Este producto no tiene reseñas'
        }
    return render(request, 'respro.html', context)

def listpro(request):
    products = Producto.objects.all().order_by('id')
    context = {
        'products': products,
    }
    return render(request, 'products.html', context)

def crearPro(request):
    if request.method=="POST":
        form = formularioProducto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("Inicio")
        else:
            messages.error(request, "Estos datos son incorrectos")
    else:
        messages.error(request, "Estos datos son incorrectos")
    form = formularioProducto()
    return render(request,'crearProducto.html',{"form":form})

def crearReview(request):
    if request.method=="POST":
        form = formularioEncuesta(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Inicio")
        else:
            messages.error(request, "Estos datos son incorrectos")
    else:
        messages.error(request, "Estos datos son incorrectos")
    form = formularioEncuesta()
    return render(request,'crearEncuesta.html',{"form":form})

def acceder(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            password =  form.cleaned_data.get("password")
            usuario = authenticate(username = nombre_usuario, password = password)
            if usuario is not None:
                login(request, usuario)
                return redirect("Inicio")
            else:
                messages.error(request,"Estos datos son incorrectos")
        else:
            messages.error(request, "Estos datos son incorrectos")
    form = AuthenticationForm()
    return render(request,'login.html',{"form":form})

def salir(request):
    logout(request)
    messages.success(request, F"Cerro sesion correctamente")
    return redirect("Inicio")


class vistaRegistro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request,'registro.html',{"form":form})


    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre = form.cleaned_data.get("username")
            messages.success(request, F"Bienveni@ a Proviews {nombre}")
            login(request,usuario)
            return redirect("Inicio")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
                return render(request, 'registro.html',{"form":form})


