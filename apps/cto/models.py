from django.db import models
from ..components.models import Bairros

# Create your models here.


class TerminaisOpticos(models.Model):
    codigo_cto = models.CharField(max_length=50, blank=True, null=True)
    rua_cto = models.CharField(max_length=100, blank=True, null=True)
    numero_rua_cto = models.CharField(max_length=20, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    bairro_cto = models.ForeignKey(Bairros, on_delete=models.DO_NOTHING, blank=True, null=True)
    pon_cto = models.CharField(max_length=100, blank=True, null=True)
    conexoes_opticas_cto = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    board_cto = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    quant_conexoes_usadas_cto = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    observacao_cto = models.TextField(blank=True, null=True)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'CTO´s'

    def __str__(self):
        return "{}".format(self.codigo_cto)


class CaixasDeEmenda(models.Model):
    codigo_caixa = models.CharField(max_length=50, blank=True, null=True)
    rua_caixa_emenda = models.CharField(max_length=100, blank=True, null=True)
    numero_rua_cto = models.CharField(max_length=20, blank=True, null=True)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Caixas de Emenda'

    def __str__(self):
        return "{}".format(self.codigo_caixa)


class NumeroPon(models.Model):
    codigoPon = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'PON'

    def __str__(self):
        return "{}".format(self.codigoPon)


class PonPorCaixaEmenda(models.Model):
    board_pon = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    pon_pon = models.CharField(max_length=100, blank=True, null=True)
    caixa_emenda = models.ForeignKey(CaixasDeEmenda, on_delete=models.DO_NOTHING)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Pon por caixa'

    def __str__(self):
        return "{} - {}".format(self.board_pon, self.pon_pon)


class Primarias(models.Model):
    board = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    pon = models.CharField(max_length=10, blank=True, null=True)
    localizacao = models.CharField(max_length=255, blank=True, null=True)
    quant_caixas = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Primárias"

    def __str__(self):
        return "{}".format(self.localizacao)


class CaixasDasPrimarias(models.Model):
    primaria = models.ForeignKey(Primarias, on_delete=models.DO_NOTHING)
    logradouro = models.CharField(max_length=255, blank=True, null=True)
    logradouro_numero = models.CharField(max_length=50, blank=True, null=True)
    codigo_caixa = models.CharField(max_length=100, blank=True, null=True)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Caixas das Primarias"

    def __str__(self):
        return "{}".format(self.logradouro)
