from django.db import models
from ..components.models import Bancos

# Create your models here.


class CategoriaPagamento(models.Model):
    nome_categoria = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categoria de Pagamentos'

    def __str__(self):
        return "{}".format(self.nome_categoria)


class TipoCusto(models.Model):
    tipo_custo = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Tipo de custo"

    def __str__(self):
        return "{}".format(self.tipo_custo)

class OrigemValores(models.Model):
    origem_valor = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Origem do valor"

    def __str__(self):
        return "{}".format(self.origem_valor)


class Pagamento(models.Model):
    motivo_pagamento = models.CharField(max_length=255, verbose_name='Motivo do pagamento')
    valor_pagamento = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    origem_valor_pagamento = models.ForeignKey(OrigemValores, on_delete=models.DO_NOTHING)
    tipo_custo_pagamento = models.ForeignKey(TipoCusto, on_delete=models.DO_NOTHING)
    data_pagamento = models.DateField()
    categoria = models.ForeignKey(CategoriaPagamento, on_delete=models.DO_NOTHING)
    status_pago = models.BooleanField(default=False, verbose_name='Pago')

    class Meta:
        verbose_name_plural = 'Pagamento'

    def __str__(self):
        return "{}".format(self.motivo_pagamento)


class AgendaPagamento(models.Model):
    motivo_pagamento = models.CharField(max_length=255, verbose_name='Motivo do pagamento')
    valor_pagamento = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    data_pagamento = models.DateField()
    categoria = models.ForeignKey(CategoriaPagamento, on_delete=models.DO_NOTHING)
    status_pago = models.BooleanField(default=False, verbose_name='Pago')

    class Meta:
        verbose_name_plural = ' Agenda Pagamento'

    def __str__(self):
        return "{}".format(self.motivo_pagamento)


class FluxoEntradasSaidas(models.Model):
    banco = models.ForeignKey(OrigemValores, on_delete=models.DO_NOTHING)
    saldoInicial = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    entradaDia = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    fluxo_data = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    SaidaDia = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    SaldoDia = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = 'Fluxo Entradas e Saídas'

    def __str__(self):
        return "{}".format(self.saldoInicial)


class DestinoValoresBoletos(models.Model):
    valor = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    destino = models.ForeignKey(Bancos, on_delete=models.DO_NOTHING)
    data_transacao = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Destino Valores Boletos"

    def __str__(self):
        return "{}".format(self.valor)


class MeiosEntregaBoletos(models.Model):
    meio_entrega = models.CharField(max_length=100, blank=True, null=True, verbose_name='Meio de entrega')

    class Meta:
        verbose_name_plural = "Meio Entrega Boletos"

    def __str__(self):
        return "{}".format(self.meio_entrega)


class ClientesEntregaBoletos(models.Model):
    nome_cliente = models.CharField(max_length=255, blank=True, null=True)
    cpf_cliente = models.CharField(max_length=50, blank=True, null=True)
    forma_entrega = models.ForeignKey(MeiosEntregaBoletos, on_delete=models.DO_NOTHING, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now=True)
    boleto_assinado = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Boletos de clientes "

    def __str__(self) -> str:
        return "{}".format(self.nome_cliente)
