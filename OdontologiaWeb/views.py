from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template import loader
from django.shortcuts import render


def saludo(request):
    nombre = persona("Juan",41)
    #doc_externo = open('/home/krb/DJango/Odontologia/OdontologiaWeb/OdontologiaWeb/plantillas/miPlantilla.html')
    #ptl = Template(doc_externo.read())
    #doc_externo.close()
    doc_externo = loader.get_template('miPlantilla.html')
    temas = ["matematica","espanol","fisica","ingles","quimica","informatica"]
    ctx = {"nombre_persona":nombre,"hora":datetime.datetime.now(),"temas":temas}
    #documento = doc_externo.render(ctx)
    return render(request,'miPlantilla.html',ctx)

def putDate(request):
    fecha_actual = datetime.datetime.now()
    documento = """<html>
    <body>
    <h1>
        La fecha actual es %s 
    </h1>
    </body>
    </html>""" %fecha_actual
    return HttpResponse(documento)

def calculaEdad(request,edad,agno):
    edad_actual = edad
    periodo = agno - 2020
    edad_futura = edad_actual + periodo
    documento = """<html>
    <body>
    <h2>
     En el anno %s tendras %s anno
    </html></body></h2> """%(agno,edad_futura)
    return HttpResponse(documento)

def cursoC(request):
    fecha_actual = datetime.datetime.now()
    return render(request,"CursoC.html",{"dameFecha":fecha_actual})

def index(request):
    return render(request,"index.html")

def index_usuarios(request):
    return render(request,'index_usuarios.html')

class persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad