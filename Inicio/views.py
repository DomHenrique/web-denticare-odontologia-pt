from django.shortcuts import render, HttpResponse
from Carrinho.carrinho import Carrinho
from Servicos.models import Servico
from Produtos.models import Produto
from Empresa.models import Unidade
from django.db import OperationalError

# Create your views here.


def Inicio(request):
    try:
        carrinho = Carrinho(request)
        servicos = Servico.objects.all()
        produtos = Produto.objects.all()
        unidades = Unidade.objects.all()
    except OperationalError:
        servicos = []
        produtos = []
        unidades = []
    
    return render(request, "Inicio/inicio.html", {
        'servicos': servicos,
        'produtos': produtos,
        'unidades': unidades
    })

def ViewProd(request, id):
    try:
        infoprod = Produto.objects.get(id=id)
        nome = infoprod.nome
        preco = infoprod.preco
        imagem = infoprod.imagem_produto
        return render (request, 'Inicio/infoprod.html', {'infoprod': infoprod, 'nome':nome, 'preco':preco, 'imagem': imagem})
    except OperationalError:
        return HttpResponse("O sitema está passando por instabilidades no banco de dados. Por favor, tente novamente mais tarde.")

