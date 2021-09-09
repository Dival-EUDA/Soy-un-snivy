from django.shortcuts import render
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