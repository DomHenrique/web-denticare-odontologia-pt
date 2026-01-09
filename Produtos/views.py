from django.shortcuts import render
from .models import Produto
from Empresa.models import Unidade
from django.db import OperationalError

# Create your views here.

def Produtos(request):
    try:
        produtos = Produto.objects.all()
        unidades = Unidade.objects.all()
        if request.method == 'POST':
            dado = request.POST.get('prod')
            produtos = Produto.objects.filter(nome__icontains = dado)
            return render(request, "Produtos/produtos.html", {'produtos': produtos, 'query': dado, 'unidades': unidades})
        else:
            return render(request, "Produtos/produtos.html", {'produtos': produtos, 'unidades': unidades})
    except OperationalError:
        return render(request, "Produtos/produtos.html", {'produtos': [], 'db_error': True, 'unidades': []})


def ViewProd(request, id):
    try:
        producto=Produto.objects.get(id=id)
        unidades = Unidade.objects.all()
        return render(request, "Produtos/infoprod.html", {"producto":producto, 'unidades': unidades})
    except OperationalError:
        return render(request, "Produtos/infoprod.html", {"producto": None, 'db_error': True, 'unidades': []})

