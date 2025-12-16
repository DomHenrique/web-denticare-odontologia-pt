from django.db import models
from django.contrib.auth import get_user_model
from Produtos.models import Produto
from django.db.models import F, Sum, FloatField

# Create your models here.
User=get_user_model()

class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def total(self):
        return self.itempedido_set.aggregate(
            total = Sum(F("preco")*F("quantidade"), output_field=FloatField)
        )["total"] 

    class Meta:
        db_table='pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering=['id']


class ItemPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    quantidade=models.IntegerField(default=1)
    criado_em=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantidade} unidades de {self.produto.nome}'
    
    class Meta:
        db_table='itens_pedido'
        verbose_name = 'Item Pedido'
        verbose_name_plural = 'Itens Pedidos'
        ordering=['id']
