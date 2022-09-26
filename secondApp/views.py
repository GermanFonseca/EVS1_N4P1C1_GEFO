from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludo(request):
    return HttpResponse("<h3>saludito</h3><br><table><tr>hola</tr><td> no se nada</td><tr>chao</tr></table><br><p>No pierdas nunca el sentido del humor y aprende a reírte de tus propios defectos.</p><ol><li>pato</li><li>gallina</li><li>caballo</li></ol><div>La capacidad para soportar la ansiedad es importante para la autorrealización del individuo y para la conquista de su entorno.</div><b>negrita</b>")

def texto(request):
    text = "<p>La realización de uno mismo solo se alcanza avanzando pese a los choques emocionales.</p><h2>titulo mas pequeño</h2>"
    return HttpResponse(text)
