from django.db import models

# Create your models here.
class Servico(models.Model):
    titulo = models.CharField(max_length=50)
    conteudo = models.CharField(max_length=70)
    imagem = models.ImageField(upload_to='servicos')
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'servico'
        verbose_name_plural = 'servicos'
    
    def __str__(self):
        return self.titulo

