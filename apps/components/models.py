from django.db import models

# Create your models here.
class PlanosInternet(models.Model):
    nome_plano = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Planos Internet'

    def __str__(self):
        return "{}".format(self.nome_plano)

class DataVencimento(models.Model):
    data = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = 'Datas Venciemento'

    def __str__(self):
        return "{}".format(self.data)


class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=100, blank=True, null=True)
    uf_cidade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Cidade'

    def __str__(self):
        return "{}".format(self.nome_cidade)



class AdicionarQuantidade(models.Model):
    quantidade = models.DecimalField(max_digits=10, decimal_places=10)
    class Meta:
        verbose_name_plural = 'Adicionar Quantidade'
    def __str__(self):
        return "{}".format(self.quantidade)
