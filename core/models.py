from django.db import models

# Create your models here.
class Dados_orcamento(models.Model):
    nome_cliente = models.CharField(max_length=100)
    endereco_logradouro = models.CharField(max_length=100)
    endereco_numero = models.IntegerField()
    endereco_cidade = models.CharField(max_length=40)
    endereco_estado = models.CharField(max_length=2)
    tipo_imovel = models.CharField(max_length=20)
    consumo_energia = models.IntegerField(blank=True, null=True)
    imagem = models.FileField(upload_to='images/orcamento', default=None, null=True, blank=True)
    data_inicial_orcamento = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, default='aguardando' )

    class Meta:
        db_table = 'orcamento'

    def __str__(self):
        return self.nome_cliente