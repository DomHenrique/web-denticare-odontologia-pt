class Carrinho:
    #Inicializar constructor
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrinho = self.session.get('carrinho')
        if not carrinho:
            carrinho = self.session['carrinho'] = {}
        
        self.carrinho = carrinho

    #Adicionar produtos ao carrinho
    def adicionar(self, produto):
        produto_id = str(produto.id)
        #Se produto nao esta no carrinho
        if(produto_id not in self.carrinho):
            self.carrinho[produto_id] = {
                "produto_id": produto.id,
                "nome": produto.nome,
                "preco": float(produto.preco),
                "quantidade": 1,
                "imagem": produto.imagem_produto.url if produto.imagem_produto else ""
            }
        #Se o produto ja esta no carrinho
        else:
            item = self.carrinho[produto_id]
            item["quantidade"] += 1
            item["preco"] = float(item["preco"]) + float(produto.preco)
            
        self.salvar_carrinho()
    
    def salvar_carrinho(self):
        self.session["carrinho"] = self.carrinho
        self.session.modified = True

    #Eliminar um produto
    def remover(self, produto):
        produto_id = str(produto.id)
        if produto_id in self.carrinho:
            del self.carrinho[produto_id]
            self.salvar_carrinho()
    
    #Subtrair unidades de um produto
    def subtrair_produto(self, produto):
        produto_id = str(produto.id)
        if produto_id in self.carrinho:
            item = self.carrinho[produto_id]
            item["quantidade"] -= 1
            item["preco"] = float(item["preco"]) - float(produto.preco)
            #Eliminar se a quantidade for menor que 1
            if item['quantidade'] < 1:
                self.remover(produto)
            else:
                self.salvar_carrinho()
    
    #Limpar o carrinho
    def limpar_carrinho(self):
        self.session['carrinho'] = {}
        self.session.modified = True
