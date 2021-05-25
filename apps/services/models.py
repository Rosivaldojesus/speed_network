from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils import timezone


class CategoriaServico(models.Model):
    nome_categoria = models.CharField(max_length=255, verbose_name='Categoria do serviço')

    class Meta:
        verbose_name_plural = 'Categoria dos serviços'

    def __str__(self):
        return "{}".format(self.nome_categoria)


class Servico(models.Model):
    contato_servico = models.CharField(max_length=255, blank=True, null=True, verbose_name='Nome do cliente')
    endereco_servico = models.TextField(blank=True, null=True, verbose_name='Endereço do serviço')
    servico_para_executar = models.TextField(blank=True, null=True, verbose_name='Serviço a fazer')
    servico_executado = models.TextField(blank=True, null=True, verbose_name='Serviço executado')
    categoria = models.ForeignKey(CategoriaServico, on_delete=models.DO_NOTHING, verbose_name='Categoria do serviço')
    data_criacao = models.DateTimeField(default=timezone.now, verbose_name='Data da criação')
    data_agendada = models.DateField(blank=True, null=True, verbose_name='Data agendada')
    hora_agendada = models.TimeField(blank=True, null=True, verbose_name='hora agendada')
    status_agendado = models.BooleanField(default=False, verbose_name='Agendado')
    material_utilizado = models.TextField(blank=True, null=True, verbose_name='Material utilizado')
    status_concluido = models.BooleanField(default=False, verbose_name='Concluído')
    data_finalizacao = models.DateField(blank=True, null=True, verbose_name='Data da conclusão')
    funcionario_servico = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)


    class Meta:
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return "{}".format(self.categoria)
