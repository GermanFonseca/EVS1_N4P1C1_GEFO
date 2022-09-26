import datetime
from re import S
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    return HttpResponse("<h1>Hola mundo!</h1>")

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b> Fecha Y Hora Actual: </b>" + str(dt)
    return HttpResponse(s)

def parrafo(request):
    return HttpResponse("<p>Fragmento de un escrito con unidad temática, que queda diferenciado del resto de fragmentos por un punto y aparte y generalmente también por llevar letra mayúscula inicial y un espacio en blanco en el margen izquierdo de alineación del texto principal de la primera línea.</p>")
