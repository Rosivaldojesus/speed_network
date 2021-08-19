from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ServicoVoip(models.Model):
    nome_usuario_voip = models.CharField(max_length=255, blank=True, null=True, verbose_name='Cliente Voip')
    cpf_usuario_voip = models.CharField(max_length=50, blank=True, null=True, verbose_name='CPF')
    usuario_voip = models.CharField(max_length=200, blank=True, null=True, verbose_name='Usuário Voip')
    senha_voip = models.CharField(max_length=50, blank=True, null=True, verbose_name='Senha Voip')
    numero_telefone_voip = models.CharField(max_length=50, blank=True, null=True, verbose_name='Telefone Voip')
    reservado_voip = models.BooleanField(default=False, verbose_name='Reservado')
    data_reserva_voip = models.DateField(blank=True, null=True, verbose_name='Data da Reserva')
    portabilidade_voip = models.BooleanField(default=False, verbose_name='Portabilidade')
    portabilidade_analise = models.BooleanField(default=False, verbose_name='Portabilidade em Análise')
    finalizado_voip = models.BooleanField(default=False, verbose_name='Finalizado')
    funcionario_reserva_voip = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='funcionário_reserva', blank=True, null=True)
    boleto_entregue = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Serviço Voip'

    def __str__(self):
        return "{}".format(self.nome_usuario_voip)