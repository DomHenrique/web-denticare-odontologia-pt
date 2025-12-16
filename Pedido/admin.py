from django.contrib import admin
from .models import Pedido, ItemPedido

# Register your models here.
admin.site.register([Pedido,ItemPedido])
