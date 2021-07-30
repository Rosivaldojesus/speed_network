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


class FabricanteEquipamentos(models.Model):
    nome_fabricante = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = 'Fabricante equipamentos'
    def __str__(self):
        return "{}".format(self.nome_fabricante)


class ModelosEquipamentos(models.Model):
    nome_modelo = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Modelos equipamentos'

    def __str__(self):
        return "{}".format(self.nome_modelo)


class Vendedores(models.Model):
    nome_vendedor = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Vendedores'

    def __str__(self):
        return "{}".format(self.nome_vendedor)


class Ruas(models.Model):
    logradouro = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    numero_baixo = models.CharField(max_length=20)
    numero_alto = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Ruas'

    def __str__(self):
        return "{}".format(self.logradouro)




class FuncionariosParaVale(models.Model):
    nome_funcionario = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Funcionarios Para Vale'

    def __str__(self):
        return "{}".format(self.nome_funcionario)