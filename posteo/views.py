from django.contrib.messages.api import error
from django.db.models.query import QuerySet
from django.forms.models import ModelForm
from django.http import request
from django.shortcuts import redirect, render
from .models import posteo
from .forms import agregarForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.db.models import Q


#las vistas donde se definen que deben hacer en cada /url/

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usarname = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
        messages.success(request, "bienvenido")
    form = AuthenticationForm
    return render(request, "registration/login.html", {"form": form})

#INICIO GET 
@login_required
def inicio(request):
    posteos = posteo.objects.all()
    
    data = {
        'posteos': posteos
    }
    return render(request, 'app/home.html', data)

#AGREGAR
@login_required
def agregar(request):
    data = {
        'form': agregarForm()
    }

    if request.method == 'POST':
        formulario = agregarForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado Correctamente!")
        else:
            data["form"] = formulario

    return render(request, 'app/agregar.html', data)

#MODIFICAR
@login_required
def modificar(request, id):

    modificar =  posteo.objects.get(id=id)

    data = {
        'form': agregarForm(instance=modificar)
    }
    if request.method == 'POST':
        formulario = agregarForm(data=request.POST, instance=modificar)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente!")
            return redirect(to="inicio")
        data["form"] = formulario
     
    return render(request, 'app/modificar.html', data)

#ELIMINAR
@login_required
def eliminar(request, id):
    eliminar =  posteo.objects.get(id=id)
    eliminar.delete()
    messages.success(request, "Eliminado Correctamente!")
    return redirect(to = "inicio")


def registro(request):
    data = {
        'form': CustomUserCreationForm
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            messages.success(request, "Se ha registrado Correctamente! :D")
            return redirect(to = "registro")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

def buscar(request):

    busqueda = request.GET.get("buscar")
    posteos = posteo.objects.all()

    if busqueda:
        posteos = posteo.objects.filter(
            Q(id__icontains = busqueda) |
            Q(base__incontains = busqueda)
        ).distinct()

    return render(request, 'app/buscar.html', {'buscar':buscar})
    

