from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='produtos', null=True, blank=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    
    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=50)
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    sku = models.CharField(max_length=10)
    preco = models.FloatField()
    marca = models.CharField(max_length=20)
    codigo_interno = models.CharField(max_length=10)
    apresentacao = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    imagem_produto = models.ImageField(upload_to='produtos', null=True, blank=True)
    disponibilidade = models.BooleanField(default=True)
    estoque = models.IntegerField()
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
    
    def __str__(self):
        return self.nome

