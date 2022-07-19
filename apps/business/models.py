from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

# Create your models here.

class VendasProdutos(models.Model):
    produto = models.CharField(_('Nome do Produto'), max_length=255)
    quantidade = models.IntegerField(_('Quantidade'))
    valor_unitario = models.DecimalField(_('Valor Unitário'), max_digits=8, decimal_places=2, default=0)
    valor_total = models.DecimalField(_('Valor Total'),max_digits=8, decimal_places=2, default=0)
    concluido = models.BooleanField(_('Concluído'), default=False)
    data_criacao = models.DateTimeField(default=timezone.now)
    ultima_alteracao = models.DateTimeField(auto_now=True)
    criador_por = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='criador_por', blank=True, null=True)
    ultima_alteracao_por = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='ultima_alteracao_por', blank=True, null=True)
    concluido_por = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='concluido_por', blank=True, null=True)
    data_conluido = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(_('Observação'),blank=True, null=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Venda de Produto'
        verbose_name_plural = 'Venda de Produtos'
        

    def __str__(self):
        return self.produto


class ComprasProdutos(models.Model):
    produto = models.CharField(_('Nome do Produto'), max_length=200)
    quantidade = models.IntegerField(_('Quantidade'), blank=True, null=True)
    valor_unitario = models.DecimalField(_('Valor Unitário'), max_digits=8, decimal_places=2, blank=True, null=True)
    valor_total = models.DecimalField(_('Valor Total'), max_digits=8, decimal_places=2, blank=True, null=True)
    concluido = models.BooleanField(_('Concluído'), default=False)
    data_criacao = models.DateTimeField(_('Data da Criação'), default=timezone.now, blank=True, null=True)
    ultima_alteracao = models.DateTimeField(_('Data da Última Alteração'), auto_now=True)
    criado_por = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='c_criado_por', blank=True, null=True)
    ultima_alteracao_por = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='c_ultima_alteracao_por', blank=True, null=True)
    concluido_por = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='c_concluido_por', blank=True, null=True)
    data_concluido = models.DateTimeField(_('Data da Conclusão'), auto_now=True, blank=True, null=True)
    observacao = models.TextField(_('Observação'),blank=True, null=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Compra de Produto'
        verbose_name_plural = 'Compra de Produtos'

    def __str__(self):
        return self.produto