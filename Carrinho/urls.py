from django.urls import path
from  .import views

app_name = 'carrinho'

urlpatterns = [
    path('adicionar/<int:producto_id>/', views.adicionar_produto, name='adicionar'),
    path('remover/<int:producto_id>/', views.remover_produto, name='remover'),
    path('subtrair/<int:producto_id>/', views.subtrair_produto, name='subtrair'),
    path('limpar/', views.limpar_carrinho, name='limpar'),
]




