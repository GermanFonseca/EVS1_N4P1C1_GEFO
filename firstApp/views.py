import datetime
from re import S
from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b> Fecha Y Hora Actual: </b>" + str(dt),"<br><div>Todos necesitamos en algún momento de nuestra vida palabras de motivación que nos den el empujón que nos falta para arriesgarnos, levantarnos, querernos, cuidarnos, o así de cliché como va a sonar: empezar de cero.</div><br><h5>pequeño</h5><title>Los Rancheros del rio de maule</title><small>Esto es un comentario</small>"
    return HttpResponse(s)

def parrafo(request):
    return HttpResponse("<p>Fragmento de un escrito con unidad temática, que queda diferenciado del resto de fragmentos por un punto y aparte y generalmente también por llevar letra mayúscula inicial y un espacio en blanco en el margen izquierdo de alineación del texto principal de la primera línea.</p><ul><li>Nombre: </li><li>Apellido: </li><li>Telefono: </li><li>correo: </li><li>direccion: </li></ul><br><h1>Linkin Park</h1><ol><li>Mike Shinoda</li><li>Chester Bennington</li><li>Brad Delson</li><li>Dave Farrell</li><li>Joe Hahn</li></ol>")
