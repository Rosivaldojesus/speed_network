from ckeditor.fields import RichTextField
from django.db import models
from ..components.models import FabricanteEquipamentos, ModelosEquipamentos

# Create your models here.
class Manuais(models.Model):
    nome_manual = models.CharField(max_length=255)
    texto_manual = RichTextField()

    class Meta:
        verbose_name_plural = 'Manuais'

    def __str__(self):
        return "{}".format(self.nome_manual)


class SenhasEquipamentos(models.Model):
    equipamento = models.CharField(max_length=100, blank=True, null=True)
    ip_equipamento = models.CharField(max_length=100, blank=True, null=True)
    login = models.CharField(max_length=100, blank=True, null=True)
    senha = models.CharField(max_length=100, blank=True, null=True)
    fabricante = models.ForeignKey(FabricanteEquipamentos, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = 'Senhas Equipamentos'

    def __str__(self):
        return "{}".format(self.equipamento)


class SenhasPorEquipamentos(models.Model):
    codigo_equipamento = models.CharField(max_length=120)
    sn_equipamento = models.CharField(max_length=100)
    equipamento = models.ForeignKey(ModelosEquipamentos, on_delete=models.DO_NOTHING)
    ip_equipamento = models.CharField(max_length=100, blank=True, null=True)
    login = models.CharField(max_length=100, blank=True, null=True)
    senha = models.CharField(max_length=100, blank=True, null=True)
    fabricante = models.ForeignKey(FabricanteEquipamentos, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = 'Senhas por Equipamentos'

    def __str__(self):
        return "{}".format(self.equipamento)


