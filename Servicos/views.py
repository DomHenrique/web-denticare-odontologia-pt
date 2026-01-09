from django.shortcuts import render
from Servicos.models import Servico
from Empresa.models import Unidade
from django.db import OperationalError

# Create your views here.


def Servicos(request):
    try:
        servicos = Servico.objects.all()
        unidades = Unidade.objects.all()
    except OperationalError:
        servicos = []
        unidades = []
    return render(request, "Servicos/servicos.html", {
        'servicos': servicos,
        'unidades': unidades
    })

