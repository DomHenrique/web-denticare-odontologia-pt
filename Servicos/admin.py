from django.contrib import admin
from .models import Servico


# Register your models here.
@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    readonly_fields = ('criado', 'atualizado')
    list_display = ('titulo', 'conteudo', 'imagem')
    search_fields = ('titulo',)
    list_per_page = 5 #Paginacao