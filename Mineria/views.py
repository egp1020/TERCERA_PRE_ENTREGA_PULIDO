from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def saludar(request):
    return HttpResponse(f"Hola Luisana Del Carmen. Hora: {datetime.now()}")

def lista_minerales(request):
    return render(request=request,template_name='Mineria/lista_minerales.html')