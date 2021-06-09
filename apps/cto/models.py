from django.db import models

# Create your models here.

class TerminaisOpticos(models.Model):
    codigo_cto = models.CharField(max_length=50, blank=True, null=True)
    rua_cto = models.CharField(max_length=100, blank=True, null=True)
    numero_rua_cto = models.CharField(max_length=20, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    pon_cto = models.CharField(max_length=100, blank=True, null=True)
    conexoes_opticas_cto = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    board_cto = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    quant_conexoes_usadas_cto =models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    observacao_cto = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'CTO´s'

    def __str__(self):
        return "{}".format(self.codigo_cto)
