from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):
    name="José Guzmán Chavarría"
    doc_externo = open("C:/Users/JoseGuzmanChavarría/OneDrive - ETC/Documentos/GitHub/Django/PingW/PingW/plantillas/saludo.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre_persona": name})
    documento = plt.render(ctx)
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("¡Adiós, mundo!")

def damefecha(request):
    fecha_actual=datetime.datetime.now()
    documento=f"Fecha y hora actual: {fecha_actual}"
    return HttpResponse(documento)