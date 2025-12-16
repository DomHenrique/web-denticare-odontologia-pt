from django.db import models
from Servicos.models import Servico

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='profissionais', null=True, blank=True)
    servicos = models.ManyToManyField(Servico, related_name='profissionais')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'

class Disponibilidade(models.Model):
    DIAS_SEMANA = (
        (0, 'Segunda-feira'),
        (1, 'Terça-feira'),
        (2, 'Quarta-feira'),
        (3, 'Quinta-feira'),
        (4, 'Sexta-feira'),
        (5, 'Sábado'),
        (6, 'Domingo'),
    )
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE, related_name='disponibilidades')
    dia_semana = models.IntegerField(choices=DIAS_SEMANA)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    intervalo_inicio = models.TimeField(null=True, blank=True)
    intervalo_fim = models.TimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Disponibilidade'
        verbose_name_plural = 'Disponibilidades'
        unique_together = ('profissional', 'dia_semana')

    def __str__(self):
        return f"{self.profissional} - {self.get_dia_semana_display()}"

class Agendamento(models.Model):
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
        ('finalizado', 'Finalizado'),
    )
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.SET_NULL, null=True, blank=True)
    data = models.DateField()
    horario = models.TimeField()
    nome_cliente = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20) # Para WhatsApp
    observacoes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        ordering = ['-data', '-horario']

    def __str__(self):
        return f"{self.nome_cliente} - {self.data} {self.horario}"
