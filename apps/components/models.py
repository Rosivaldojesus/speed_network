from django.db import models


# Create your models here.


class PlanosInternet(models.Model):
    nome_plano = models.CharField(max_length=30)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Planos Internet'

    def __str__(self):
        return "{}".format(self.nome_plano)


"""
------------------------------------------------------------------------------------------------------------------------
Datas de vencimentos
------------------------------------------------------------------------------------------------------------------------
"""


class DataVencimento(models.Model):
    data = models.CharField(max_length=100, verbose_name="Data de Vencimento")

    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Datas Vencimento'

    def __str__(self):
        return "{}".format(self.data)


"""
------------------------------------------------------------------------------------------------------------------------
Lista das cidades
------------------------------------------------------------------------------------------------------------------------
"""


class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=100, blank=True, null=True)
    uf_cidade = models.CharField(max_length=2, blank=True, null=True)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Cidade'

    def __str__(self):
        return "{}".format(self.nome_cidade)


"""
------------------------------------------------------------------------------------------------------------------------
Quantidades
------------------------------------------------------------------------------------------------------------------------
"""


class AdicionarQuantidade(models.Model):
    quantidade = models.DecimalField(max_digits=10, decimal_places=10)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Adicionar Quantidade'

    def __str__(self):
        return "{}".format(self.quantidade)


"""
------------------------------------------------------------------------------------------------------------------------
Lista de fabricantes de ONU
------------------------------------------------------------------------------------------------------------------------
"""


class FabricanteEquipamentos(models.Model):
    nome_fabricante = models.CharField(max_length=255)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Fabricante equipamentos'

    def __str__(self):
        return "{}".format(self.nome_fabricante)


"""
------------------------------------------------------------------------------------------------------------------------
Lista de modelos de ONU
------------------------------------------------------------------------------------------------------------------------
"""


class ModelosEquipamentos(models.Model):
    nome_modelo = models.CharField(max_length=255)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Modelos equipamentos'

    def __str__(self):
        return "{}".format(self.nome_modelo)


"""
------------------------------------------------------------------------------------------------------------------------
Lista de Vendedores
------------------------------------------------------------------------------------------------------------------------
"""


class Vendedores(models.Model):
    nome_vendedor = models.CharField(max_length=255)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Vendedores'

    def __str__(self):
        return "{}".format(self.nome_vendedor)


"""
------------------------------------------------------------------------------------------------------------------------
Lista de Funcionários que podem pegar Vale-Refeição
------------------------------------------------------------------------------------------------------------------------
"""


class FuncionariosParaVale(models.Model):
    nome_funcionario = models.CharField(max_length=255, null=True, blank=True)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Funcionarios Para Vale'

    def __str__(self):
        return "{}".format(self.nome_funcionario)


"""
------------------------------------------------------------------------------------------------------------------------
Lista dos bancos
------------------------------------------------------------------------------------------------------------------------
"""


class Bancos(models.Model):
    nome_banco = models.CharField(max_length=100)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Banco"
    
    def __str__(self) -> str:
        return "{}".format(self.nome_banco)


"""
------------------------------------------------------------------------------------------------------------------------
Lista dos bairros
------------------------------------------------------------------------------------------------------------------------
"""


class Bairros(models.Model):
    nome_bairro = models.CharField(max_length=100)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Bairros"

    def __str__(self):
        return "{}".format(self.nome_bairro)


"""
------------------------------------------------------------------------------------------------------------------------
Lista das ruas que possuem serviços da SPEED NETWORK TELECOM
------------------------------------------------------------------------------------------------------------------------
"""


class Ruas(models.Model):
    logradouro = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    bairro_ruas = models.ForeignKey(Bairros, on_delete=models.DO_NOTHING, blank=True, null=True)
    cep = models.CharField(max_length=100)
    numero_baixo = models.CharField(max_length=20)
    numero_alto = models.CharField(max_length=20)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Ruas'

    def __str__(self):
        return "{}".format(self.logradouro)
