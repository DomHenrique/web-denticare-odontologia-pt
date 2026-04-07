from django.shortcuts import render, get_object_or_404
from .models import Produto
from Empresa.models import Unidade

# Create your views here.

def Produtos(request):
    produtos = Produto.objects.all()
    unidades = Unidade.objects.all()
    if request.method == 'POST':
        dado = request.POST.get('prod')
        produtos = Produto.objects.filter(nome__icontains=dado)
        return render(request, "Produtos/produtos.html", {'produtos': produtos, 'query': dado, 'unidades': unidades})
    else:
        return render(request, "Produtos/produtos.html", {'produtos': produtos, 'unidades': unidades})

def ViewProd(request, id):
    producto = get_object_or_404(Produto, id=id)
    unidades = Unidade.objects.all()
    return render(request, "Produtos/infoprod.html", {"producto": producto, 'unidades': unidades})
