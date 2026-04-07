from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Carrinho.carrinho import Carrinho
from Pedido.models import ItemPedido, Pedido
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

# Agrega esta función antes de procesar_pedido
def formatar_itens_pedido(itens_pedido):
    return ", ".join([f"{item.quantidade} unidades de {item.produto.nome}" for item in itens_pedido])

@login_required(login_url="autenticacao/login")
def processar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carrinho = Carrinho(request)
    itens_pedido = list()
    for key, value in carrinho.carrinho.items():
        itens_pedido.append(ItemPedido(
            produto_id=key,
            quantidade = value['quantidade'],
            user=request.user,
            pedido = pedido
        ))

    ItemPedido.objects.bulk_create(itens_pedido)

    # Usa la nueva función aquí
    itens_texto = formatar_itens_pedido(itens_pedido)

    enviar_email(
        pedido=pedido,
        itens_pedido=itens_pedido,
        itens_texto=itens_texto,  # Agrega esto
        nomeusuario=request.user.username,
        emailusuario=request.user.email
    )

    messages.success(request, 'O pedido foi criado corretamente')

    return redirect("../produtos")

from django.conf import settings

def enviar_email(**kwargs):
    assunto = "Novo pedido DentiCare - Obrigado"
    mensagem = render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "itens_pedido": kwargs.get("itens_pedido"),
        "itens_texto": kwargs.get("itens_texto"),
        "nomeusuario": kwargs.get("nomeusuario"),
    })

    mensagem_texto = strip_tags(mensagem)
    from_email = settings.EMAIL_HOST_USER
    to = settings.CONTACT_EMAIL

    send_mail(assunto, mensagem_texto, from_email, [to], html_message=mensagem)