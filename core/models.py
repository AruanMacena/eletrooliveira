from django.db import models
from django.contrib.auth.models import User
from public.utils.estados_brasileiros import ESTADOS_BRASILEIROS


# Create your models here.
class Dados_orcamento(models.Model):
    nome_cliente = models.CharField(max_length=100, verbose_name= 'Nome do cliente')
    endereco_logradouro = models.CharField(max_length=100, verbose_name='Logradouro')
    endereco_numero = models.IntegerField(verbose_name='Número')
    endereco_cidade = models.CharField(max_length=40, verbose_name='Cidade')
    endereco_estado = models.CharField(max_length=2, verbose_name='Estado',choices=ESTADOS_BRASILEIROS, default='SP')
    tipo_imovel = models.CharField(max_length=20, )
    consumo_energia = models.IntegerField(blank=True, null=True)
    imagem = models.FileField(upload_to='images/orcamento', default=None, null=True, blank=True)
    data_inicial_orcamento = models.DateTimeField(auto_now=True, verbose_name= 'Data do orçamento')
    status = models.CharField(max_length=30, default='aguardando')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orcamento'

    def __str__(self):
        return self.nome_cliente