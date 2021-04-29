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



class Pagamento(models.Model):
    nome_pagamento = models.CharField(max_length=255)
    valor_pagamento = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    data_pagamento = models.DateTimeField()
    data_lancamento = models.DateTimeField(default=timezone.now)
    categoria = models.ForeignKey(CategoriaPagamento, on_delete=models.DO_NOTHING)
    motivo_pagamento = RichTextField()

    class Meta:
        verbose_name_plural = 'Pagamento'

    def __str__(self):
        return "{}".format(self.nome_pagamento)