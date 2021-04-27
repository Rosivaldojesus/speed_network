from django.db import models

# Create your models here.




class Produto(models.Model):
    nome_produto = models.CharField(max_length=100, blank=True, null=True)
    marca_produto = models.CharField(max_length=100, blank=True, null=True)
    modelo_produto = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return "{}".format(self.nome_produto)


class EntradaProduto(models.Model):
    quantidade = models.DecimalField(max_digits=10, decimal_places=0)
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = 'Entrada de Produtos'

    def __str__(self):
        return "{}".format(self.quantidade)


class SaidaProduto(models.Model):
    quantidade = models.DecimalField(max_digits=10, decimal_places=0)
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = 'Saída de Produtos'

    def __str__(self):
        return "{}".format(self.quantidade)

