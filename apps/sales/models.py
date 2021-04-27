from django.db import models
from ..components.models import PlanosInternet

# Create your models here.

class Instalacao(models.Model):
    nome_cliente = models.CharField(max_length=255, blank=True, null=True)
    cpf_cliente = models.CharField(max_length=14, blank=True, null=True)
    rg_cliente = models.CharField(max_length=20, blank=True, null=True)
    rua_cliente = models.CharField(max_length=100, blank=True, null=True)
    bairro_cliente = models.CharField(max_length=100, blank=True, null=True)
    numero_endereco_cliente = models.CharField(max_length=100, blank=True, null=True)
    cidade_cliente = models.CharField(max_length=100, blank=True, null=True)
    uf_cliente = models.CharField(max_length=2, blank=True, null=True)
    telefone_cliente = models.CharField(max_length=10, blank=True, null=True)
    email_cliente = models.CharField(max_length=100, blank=True, null=True)
    planos_instalacao = models.ForeignKey(PlanosInternet, on_delete=models.DO_NOTHING)


    class Meta:
        verbose_name_plural = 'Instalação'

    def __str__(self):
        return "{}".format(self.nome_cliente)