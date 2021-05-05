from django.utils import timezone
from ..components.models import PlanosInternet, Cidade, DataVencimento
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Instalacao(models.Model):
    nome_cliente = models.CharField(max_length=255, blank=True, null=True, verbose_name='Primeiro nome')
    sobrenome_cliente = models.CharField(max_length=255, blank=True, null=True, verbose_name='Sobrenome')
    cpf_cliente = models.CharField(max_length=14, blank=True, null=True, verbose_name='CPF')
    rg_cliente = models.CharField(max_length=20, blank=True, null=True, verbose_name='RG')
    cep_cliente = models.CharField(max_length=20, blank=True, null=True, verbose_name='CEP')
    rua_cliente = models.CharField(max_length=100, blank=True, null=True, verbose_name='Rua')
    bairro_cliente = models.CharField(max_length=100, blank=True, null=True, verbose_name='Bairro')
    numero_endereco_cliente = models.CharField(max_length=100, blank=True, null=True, verbose_name='Nº.')
    complemento_endereco_cliente = models.CharField(max_length=255, blank=True, null=True, verbose_name='Complemento')
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING, verbose_name='Cidade')
    telefone_cliente = models.CharField(max_length=10, blank=True, null=True, verbose_name='Telefone Celular')
    email_cliente = models.CharField(max_length=100, blank=True, null=True, verbose_name='E-mail')
    planos_instalacao = models.ForeignKey(PlanosInternet, on_delete=models.DO_NOTHING, verbose_name='Planos Instalação')
    data_vencimento = models.ForeignKey(DataVencimento, on_delete=models.DO_NOTHING, verbose_name='Data de Vencimento')
    data_criacao = models.DateTimeField(default=timezone.now)
    concluido = models.BooleanField(default=False)
    data_instalacao = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, verbose_name='Data da Instalação')
    hora_instalacao = models.TimeField(auto_now_add=False, auto_now=False, blank=True, null=True, verbose_name='Hora da Instalação')
    observacao_instalacao = RichTextField(blank=True, null=True, verbose_name='Observação')

    class Meta:
        verbose_name_plural = 'Instalação'

    def __str__(self):
        return "{}".format(self.nome_cliente)