from django.shortcuts import render
from .models import Produto
# Create your views here.

def Produtos(request):
    produtos = Produto.objects.all()
    if  request.method == 'POST':
        dado = request.POST.get('prod')
        produtos = Produto.objects.filter(nome__icontains = dado)
        return render(request, "Produtos/produtos.html", {'produtos': produtos, 'query': dado})
    else:
        return render(request, "Produtos/produtos.html", {'produtos': produtos})


def ViewProd(request, id):
    producto=Produto.objects.get(id=id)
    return render(request, "Produtos/infoprod.html", {"producto":producto})
