from django.shortcuts import render

# Create your views here.

def init(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')