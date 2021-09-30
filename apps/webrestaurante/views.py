from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def init(request):
    allcomida = Comida.objects.all()
    allbebida = Bebida.objects.all()
    allpostre = Postre.objects.all()
    return render(request, 'index.html', {'allcomida':allcomida, 'allbebida':allbebida, 'allpostre':allpostre})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def ejemploform(request):
    if request.method == "POST":
        Nombre = request.POST.get('nombre')
        Apellido = request.POST.get('apellido')
        Fecha_nacimiento = request.POST.get('fecha_nacimiento')
        Salario = request.POST.get('salario')
        Telefono = request.POST.get('telefono')
        Direccion = request.POST.get('direccion')
        print(Nombre + ' ' + Apellido + ' ' + Fecha_nacimiento)
        print(Salario + ' ' + Telefono + ' ' + Direccion)

        model_empleado = empleado(nombre=Nombre,
                                  apellido=Apellido,
                                  fecha_nacimiento=Fecha_nacimiento,
                                  salario=Salario,
                                  telefono=Telefono,
                                  direccion=Direccion)
        model_empleado.save()
        return redirect('webrestaurante:init')
    elif request.method == "GET":
        return render(request, 'ejemploform.html')

