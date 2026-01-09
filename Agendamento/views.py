from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .models import Profissional, Disponibilidade, Agendamento
from Servicos.models import Servico
from Empresa.models import Unidade
from datetime import datetime, timedelta, date
import json

from django.db import OperationalError

@login_required
def agendar(request):
    try:
        servicos = Servico.objects.all()
        unidades = Unidade.objects.all()
    except OperationalError:
        servicos = []
        unidades = []
    
    context = {
        'servicos': servicos,
        'unidades': unidades,
        'db_error': True if not servicos else False
    }
    return render(request, 'agendamento/index.html', context)


def get_profissionais(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id)
    profissionais = servico.profissionais.all()
    # Si no hay profesionales específicos, mostrar todos o manejar lógica
    # Por ahora asumimos que el servicio tiene profesionales asignados
    data = [{'id': p.id, 'nome': p.nome, 'especialidade': p.especialidade} for p in profissionais]
    return JsonResponse(data, safe=False)

def get_dias_disponiveis(request):
    profissional_id = request.GET.get('profissional_id')
    if not profissional_id:
         return JsonResponse([], safe=False)
    
    profissional = get_object_or_404(Profissional, id=profissional_id)
    disponibilidades = profissional.disponibilidades.all()
    dias_semana = [d.dia_semana for d in disponibilidades]
    
    # Generar próximos 30 días disponibles
    dias_disponiveis = []
    hoje = date.today()
    for i in range(30):
        dia = hoje + timedelta(days=i)
        if dia.weekday() in dias_semana:
            dias_disponiveis.append({
                'data': dia.isoformat(),
                'display': dia.strftime('%d/%m/%Y'),
                'dia_semana': dia.strftime('%A')
            })
            
    return JsonResponse(dias_disponiveis, safe=False)

def get_horarios(request):
    profissional_id = request.GET.get('profissional_id')
    data_str = request.GET.get('data')
    
    if not profissional_id or not data_str:
        return JsonResponse([], safe=False)

    profissional = get_object_or_404(Profissional, id=profissional_id)
    data_obj = datetime.strptime(data_str, '%Y-%m-%d').date()
    dia_semana = data_obj.weekday()
    
    try:
        disponibilidade = profissional.disponibilidades.get(dia_semana=dia_semana)
    except Disponibilidade.DoesNotExist:
        return JsonResponse([], safe=False)

    horarios = []
    atual = datetime.combine(data_obj, disponibilidade.hora_inicio)
    fim = datetime.combine(data_obj, disponibilidade.hora_fim)
    
    intervalo_inicio = None
    intervalo_fim = None
    if disponibilidade.intervalo_inicio and disponibilidade.intervalo_fim:
        intervalo_inicio = datetime.combine(data_obj, disponibilidade.intervalo_inicio)
        intervalo_fim = datetime.combine(data_obj, disponibilidade.intervalo_fim)

    # Otimização: Buscar todos os agendamentos ocupados em uma única consulta
    agendamentos_ocupados = set(Agendamento.objects.filter(
        profissional=profissional,
        data=data_obj,
        status__in=['confirmado', 'pendente']
    ).values_list('horario', flat=True))

    while atual < fim:
        agora_time = atual.time()
        
        # Verificar si está en intervalo
        in_break = False
        if intervalo_inicio and intervalo_fim:
            if intervalo_inicio <= atual < intervalo_fim:
                in_break = True
        
        # Verificar si ya está agendado (usando o set em memória)
        ocupado = agora_time in agendamentos_ocupados

        if not in_break and not ocupado:
            horarios.append(atual.strftime('%H:%M'))
        
        atual += timedelta(minutes=30) # Intervalo de 30 min fijo por ahora
        
    return JsonResponse(horarios, safe=False)

def confirmar_agendamento(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            agendamento = Agendamento.objects.create(
                servico_id=data['servico_id'],
                profissional_id=data['profissional_id'],
                data=data['data'],
                horario=data['horario'],
                nome_cliente=data['nome'],
                telefone=data['whatsapp'],
                observacoes=data.get('observacoes', ''),
                status='pendente'
            )
            return JsonResponse({'status': 'success', 'id': agendamento.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error'}, status=405)
