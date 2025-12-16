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
        #Se produto nao esta no carrinho
        if(str(produto.id) not in self.carrinho.keys()):
            self.carrinho[producto.id] = {
                "produto_id": produto.id,
                "nome":produto.nome,
                "preco": str(producto.preco),
                "quantidade": 1,
                "imagem": produto.imagem_producto.url
            }
        #Se o produto ja esta no carrinho
        else:
            for key, value in self.carrinho.items():
                if key == str(produto.id):
                    value["quantidade"]=value["quantidade"]+1
                    value["preco"]=float(value["preco"])+producto.preco
                    break
        self.salvar_carrinho()

    
    def salvar_carrinho(self):
        self.session["carrinho"] = self.carrinho
        self.session.modified = True


    #Eliminar um produto
    def remover(self, produto):
        producto.id = str(producto.id)
        if produto.id in self.carrinho:
            del self.carrinho[producto.id]
            self.salvar_carrinho()
    
    #Subtrair unidades de um produto
    def subtrair_produto(self, produto):
        for key, value in self.carrinho.items():
                if key == str(producto.id):
                    value["quantidade"]=value["quantidade"]-1
                    value["preco"]=float(value["preco"])-producto.preco
                    #Eliminar se a quantidade for menor que 1
                    if  value['quantidade'] < 1:
                        self.remover(produto)
                    break
        self.salvar_carrinho()
    
    #Limpar o carrinho
    def limpar_carrinho(self):
        self.session['carrinho'] = {}
        self.session.modified = True

