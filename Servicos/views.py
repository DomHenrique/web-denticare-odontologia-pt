from django.shortcuts import render
from Servicos.models import Servico
from Empresa.models import Unidade

# Create your views here.

def Servicos(request):
    servicos = Servico.objects.all()
    unidades = Unidade.objects.all()
    return render(request, "Servicos/servicos.html", {
        'servicos': servicos,
        'unidades': unidades
    })
