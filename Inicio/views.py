from django.shortcuts import render, HttpResponse
from Carrinho.carrinho import Carrinho
from Servicos.models import Servico
from Produtos.models import Produto

# Create your views here.


def Inicio(request):
    carrinho = Carrinho(request)
    servicos = Servico.objects.all()
    produtos = Produto.objects.all()

    return render(request, "Inicio/inicio.html",{'servicos':servicos, 'produtos':produtos})

def ViewProd(request, id):
    infoprod = Produto.objects.get(id=id)
    nome = infoprod.nome
    preco = infoprod.preco
    imagem = infoprod.imagem_produto
    return render (request, 'Inicio/infoprod.html', {'infoprod': infoprod, 'nome':nome, 'preco':preco, 'imagem': imagem})
