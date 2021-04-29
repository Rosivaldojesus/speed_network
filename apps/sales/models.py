from django.utils import timezone
from ..components.models import PlanosInternet, Cidade
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Instalacao(models.Model):
    nome_cliente = models.CharField(max_length=255, blank=True, null=True)
    sobrenome_cliente = models.CharField(max_length=255, blank=True, null=True)
    cpf_cliente = models.CharField(max_length=14, blank=True, null=True)
    rg_cliente = models.CharField(max_length=20, blank=True, null=True)
    cep_cliente = models.CharField(max_length=20, blank=True, null=True)
    rua_cliente = models.CharField(max_length=100, blank=True, null=True)
    bairro_cliente = models.CharField(max_length=100, blank=True, null=True)
    numero_endereco_cliente = models.CharField(max_length=100, blank=True, null=True)
    complemento_endereco_cliente = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING)
    telefone_cliente = models.CharField(max_length=10, blank=True, null=True)
    email_cliente = models.CharField(max_length=100, blank=True, null=True)
    planos_instalacao = models.ForeignKey(PlanosInternet, on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField(default=timezone.now)
    instalando = models.BooleanField(default=False)
    concluido = models.BooleanField(default=False)
    data_instalacao = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    hora_instalacao = models.TimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    observacao_instalacao = RichTextField(blank=True, null=True)


    class Meta:
        verbose_name_plural = 'Instalação'

    def __str__(self):
        return "{}".format(self.nome_cliente)