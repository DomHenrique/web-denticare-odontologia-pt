from django.contrib import admin
from .models import Unidade

@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'cidade', 'estado', 'telefone', 'ordem')
    list_filter = ('tipo', 'estado')
    search_fields = ('nome', 'endereco', 'cidade')
    ordering = ('ordem', 'nome')
