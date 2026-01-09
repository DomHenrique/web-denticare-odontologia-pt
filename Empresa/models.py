from django.db import models

class Unidade(models.Model):
    TIPO_CHOICES = (
        ('matriz', 'Matriz'),
        ('filial', 'Filial'),
    )
    nome = models.CharField(max_length=100, verbose_name="Nome da Unidade")
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='filial')
    endereco = models.CharField(max_length=255, verbose_name="Endereço")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")
    estado = models.CharField(max_length=2, verbose_name="Estado (UF)", default="SP")
    email = models.EmailField(verbose_name="E-mail de Contato")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    whatsapp = models.CharField(max_length=20, verbose_name="WhatsApp")
    mapa_url = models.URLField(max_length=500, verbose_name="URL do Google Maps", blank=True, null=True)
    ordem = models.IntegerField(default=0, help_text="Ordem de exibição no site")

    class Meta:
        verbose_name = "Unidade"
        verbose_name_plural = "Unidades"
        ordering = ['ordem', 'nome']

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"
