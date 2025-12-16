from django.contrib import admin
from django.utils.html import format_html
from django.urls import path
from django.template.response import TemplateResponse
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
import json
from .models import Profissional, Disponibilidade, Agendamento

class DisponibilidadeInline(admin.TabularInline):
    model = Disponibilidade
    extra = 1

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especialidade')
    filter_horizontal = ('servicos',)
    inlines = [DisponibilidadeInline]

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('nome_cliente', 'servico', 'data', 'horario', 'status_colored', 'profissional')
    list_filter = ('status', 'data', 'profissional')
    search_fields = ('nome_cliente', 'telefone')
    date_hierarchy = 'data'
    actions = ['mark_confirmed', 'mark_cancelled']
    change_list_template = 'admin/agendamento/change_list.html'

    def status_colored(self, obj):
        colors = {
            'pendente': 'orange',
            'confirmado': 'green',
            'cancelado': 'red',
            'finalizado': 'blue',
        }
        color = colors.get(obj.status, 'black')
        return format_html(
            '<span style="color: white; background-color: {}; padding: 3px 10px; border-radius: 10px; font-weight: bold;">{}</span>',
            color,
            obj.get_status_display()
        )
    status_colored.short_description = 'Status'

    def mark_confirmed(self, request, queryset):
        queryset.update(status='confirmado')
    mark_confirmed.short_description = "Marcar selecionados como Confirmado"

    def mark_cancelled(self, request, queryset):
        queryset.update(status='cancelado')
    mark_cancelled.short_description = "Marcar selecionados como Cancelado"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('calendar/', self.admin_site.admin_view(self.calendar_view), name='agendamento_calendar'),
        ]
        return custom_urls + urls

    def calendar_view(self, request):
        # Fetch events for calendar
        agendamentos = Agendamento.objects.all()
        events = []
        for a in agendamentos:
            color = {'pendente': '#ffc107', 'confirmado': '#28a745', 'cancelado': '#dc3545', 'finalizado': '#007bff'}.get(a.status, '#6c757d')
            events.append({
                'title': f"{a.horario.strftime('%H:%M')} - {a.nome_cliente}",
                'start': f"{a.data.isoformat()}T{a.horario.strftime('%H:%M:%S')}",
                'url': f"/admin/Agendamento/agendamento/{a.id}/change/",
                'color': color,
                'status': a.status
            })
        
        context = dict(
            self.admin_site.each_context(request),
            events=json.dumps(events, cls=DjangoJSONEncoder),
            title="Agenda Visual"
        )
        return TemplateResponse(request, "admin/agendamento/calendar.html", context)
