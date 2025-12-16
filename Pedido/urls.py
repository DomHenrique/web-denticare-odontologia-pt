from django.urls import path
from . import views


urlpatterns = [
    path('', views.processar_pedido, name = 'processar_pedido'),
]



