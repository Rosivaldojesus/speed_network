from datetime import datetime, date

from django.utils import timezone
from ..components.models import PlanosInternet, Cidade, DataVencimento, Vendedores
from django.db import models
from django.contrib.auth.models import User
from ..components.models import FuncionariosParaVale
from ckeditor.fields import RichTextField
from django.urls import reverse


# Create your models here.

class Instalacao(models.Model):
    nome_cliente = models.CharField(max_length=255, blank=True, null=True, verbose_name='Primeiro nome')
    sobrenome_cliente = models.CharField(max_length=255, blank=True, null=True, verbose_name='Sobrenome')
    cpf_cliente = models.CharField(max_length=20, blank=True, null=True, verbose_name='CPF')
    cep_cliente = models.CharField(max_length=20, blank=True, null=True, verbose_name='CEP')
    rua_cliente = models.CharField(max_length=100, blank=True, null=True, verbose_name='Rua')
    bairro_cliente = models.CharField(max_length=100, blank=True, null=True, verbose_name='Bairro')
    numero_endereco_cliente = models.CharField(max_length=100, blank=True, null=True, verbose_name='Nº.')
    complemento_endereco_cliente = models.CharField(max_length=255, blank=True, null=True, verbose_name='Complemento')
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING, verbose_name='Cidade')
    telefone1_cliente = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefone 1')
    telefone2_cliente = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefone 2')
    email_cliente = models.CharField(max_length=100, blank=True, null=True, verbose_name='E-mail')
    planos_instalacao = models.ForeignKey(PlanosInternet, on_delete=models.DO_NOTHING, verbose_name='Planos Instalação')
    data_vencimento = models.ForeignKey(DataVencimento, on_delete=models.DO_NOTHING, verbose_name='Data de Vencimento')
    data_criacao = models.DateTimeField(default=timezone.now)
    status_agendada = models.BooleanField(default=False)
    concluido = models.BooleanField(default=False)
    data_instalacao = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, verbose_name='Data da Instalação')
    hora_instalacao = models.TimeField(auto_now_add=False, auto_now=False, blank=True, null=True, verbose_name='Hora da Instalação')
    material_utilizado = models.TextField(blank=True, null=True, verbose_name='Material utilizado')
    funcionario_instalacao = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    data_concluido = models.DateTimeField(null=True, blank=True)
    data_finalizacao = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, verbose_name='Data da Finalização')
    boleto_entregue = models.BooleanField(default=False)
    observacao_instalacao = models.TextField(blank=True, null=True, verbose_name='Observação')
    instalacao_criado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='instalacao_criado_por', blank=True, null=True)
    instalacao_finalizado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='instalacao_finalizado_por', blank=True, null=True)
    instalacao_vendedor = models.ForeignKey(Vendedores, on_delete=models.DO_NOTHING, verbose_name='Vendedores')


    class Meta:
        verbose_name_plural = 'Instalação'

    def __str__(self):
        return "{}".format(self.nome_cliente)


class ClientesVoip(models.Model):
    nome_usuario_voip = models.CharField(max_length=255, blank=True, null=True, verbose_name='Cliente Voip')
    cpf_usuario_voip = models.CharField(max_length=50, blank=True, null=True, verbose_name='CPF')
    usuario_voip = models.CharField(max_length=200, blank=True, null=True, verbose_name='Usuário Voip')
    senha_voip = models.CharField(max_length=50, blank=True, null=True, verbose_name='Senha Voip')
    numero_telefone_voip = models.CharField(max_length=50, blank=True, null=True, verbose_name='Telefone Voip')
    reservado_voip = models.BooleanField(default=False, verbose_name='Reservado')
    data_reserva_voip = models.DateField(blank=True, null=True, verbose_name='Data da Reserva')
    portabilidade_voip = models.BooleanField(default=False, verbose_name='Portabilidade')
    finalizado_voip = models.BooleanField(default=False, verbose_name='Finalizado')
    funcionario_reserva_voip = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='funcionario_reserva_voip', blank=True, null=True)


    class Meta:
        verbose_name_plural = 'Clientes Voip'

    def __str__(self):
        return "{}".format(self.nome_usuario_voip)



class ValeRefeicao(models.Model):
    nome_funcionario = models.CharField(max_length=255)
    valor_vale = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    data_vale = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    status_pago = models.BooleanField(default=False, verbose_name='Pago')

    class Meta:
        verbose_name_plural = " Vale Refeição"

    def __str__(self):
        return "{}".format(self.nome_funcionario)




class Cancelamentos(models.Model):
    nome = models.CharField(max_length=255, blank=True, null=True, verbose_name='Nome Cliente')
    cpf = models.CharField(max_length=30, verbose_name='CPF do Cliente')
    endereco = models.CharField(max_length=255, verbose_name='Rua do Cliente')
    cep = models.CharField(max_length=255, verbose_name='CEP do Cliente')
    bairro = models.CharField(max_length=255, verbose_name='Bairro do Cliente')
    numero = models.CharField(max_length=255, verbose_name='Número do Cliente')


    atendente = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Atendente')
    plano_internet = models.CharField(max_length=255, blank=True, null=True)
    motivo = models.CharField(max_length=255, blank=True, null=True)
    data = models.DateField(blank=True, null=True, verbose_name='Data do serviço')
    data_criacao = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('detalhes-detail', kwargs={'pk': self.pk})


    class Meta:
        verbose_name_plural = "Cancelamentos"

    def __str__(self):
        return "{}".format(self.nome)