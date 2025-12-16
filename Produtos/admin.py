from django.contrib import admin
from .models import Categoria, Produto

# Register your models here.
admin.site.site_header = 'DENTICARE'
admin.site.site_title = 'DENTICARE'
admin.site.index_title = 'Gestao de produtos - DentiCare'

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('criado', 'atualizado')
    list_display = ('nome', 'imagem', 'criado', 'atualizado')
    search_fields = ('nome',)
    list_per_page = 5 #Paginacao

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    readonly_fields = ('criado', 'atualizado')
    list_display = ('nome', 'categorias', 'sku', 'preco', 'marca', 'codigo_interno', 'apresentacao','descricao', 'imagem_produto', 'estoque', 'disponibilidade', 'criado', 'atualizado')
    search_fields = ('nome',)
    list_per_page = 5 #Paginacao
#alt+z
