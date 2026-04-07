from django.shortcuts import render, HttpResponse, get_object_or_404
from Carrinho.carrinho import Carrinho
from Servicos.models import Servico
from Produtos.models import Produto
from Empresa.models import Unidade

# Create your views here.

def Inicio(request):
    carrinho = Carrinho(request)
    servicos = Servico.objects.all()
    produtos = Produto.objects.all()
    unidades = Unidade.objects.all()
    
    return render(request, "Inicio/inicio.html", {
        'servicos': servicos,
        'produtos': produtos,
        'unidades': unidades
    })

def ViewProd(request, id):
    infoprod = get_object_or_404(Produto, id=id)
    nome = infoprod.nome
    preco = infoprod.preco
    imagem = infoprod.imagem_produto
    return render(request, 'Inicio/infoprod.html', {'infoprod': infoprod, 'nome': nome, 'preco': preco, 'imagem': imagem})
