from django.db import OperationalError

def valor_total_carrinho(request):
    total = 0
    quantidade = 0
    try:
        if request.user.is_authenticated:
            if 'carrinho' in request.session:
                for key, value in request.session["carrinho"].items():
                    total = total+float(value['preco'])
                    quantidade = quantidade+int(value['quantidade'])
        else:
            total = 'Voce deve fazer login'
    except OperationalError:
        total = 0
        quantidade = 0
    
    return {'valor_total_carrinho':total, 'total_produto':quantidade}



