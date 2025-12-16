from django.shortcuts import redirect
from .carrinho import Carrinho
from Produtos.models import Produto
from django.http import HttpResponse
# Create your views here.

#Adicionar um produto
def adicionar_produto(request, produto_id):
    carrinho = Carrinho(request)
    produto = Produto.objects.get(id=produto_id)
    carrinho.adicionar(produto=produto)
    return redirect('produtos')


#Remover um produto
def remover_produto(request, produto_id):
    carrinho = Carrinho(request)
    produto = Produto.objects.get(id=produto_id)
    carrinho.remover(produto=produto)
    return redirect('produtos')

#Subtrair um produto
def subtrair_produto (request, produto_id):
    carrinho = Carrinho(request)
    produto = Produto.objects.get(id=produto_id)
    carrinho.subtrair_produto(produto=produto)
    return redirect('produtos')

#Limpar carrinho
def limpar_carrinho(request,):
    carrinho = Carrinho(request)
    carrinho.limpar_carrinho()
    return redirect('produtos')