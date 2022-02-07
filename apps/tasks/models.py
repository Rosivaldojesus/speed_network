from django.db import models
from django.utils import timezone

# Create your models here.


class Tarefas(models.Model):
    nome_tarefa = models.TextField(verbose_name='Nome da Tarefa')
    data_criacao = models.DateTimeField(default=timezone.now)
    analisando = models.BooleanField(default=False)
    previsao_conclusao = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True,
                                          verbose_name='Previsao de Conclusão')
    concluido = models.BooleanField(default=False)
    data_conclusao = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True,
                                      verbose_name='Data da  Conclusão')
    observacao = models.TextField(blank=True, null=True, verbose_name='Observação')

    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Tarefas'

    def __str__(self):
        return "{}".format(self.nome_tarefa)
