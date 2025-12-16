from django.shortcuts import render
from Servicos.models import Servico
# Create your views here.


def Servicos(request):
    servicos = Servico.objects.all()
    return render(request, "Servicos/servicos.html", {'servicos': servicos})
