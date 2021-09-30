from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

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

    class Meta:
        verbose_name_plural = 'Fluxo Entradas e Saídas'

    def __str__(self):
        return "{}".format(self.saldoInicial)