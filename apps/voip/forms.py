
from django import forms
from django.contrib.auth.models import User
from .models import ServicoVoip


class AdicionarNumeroVoipForm(forms.ModelForm):
    class Meta:
        model = ServicoVoip
        fields = ['usuario_voip',
                  'senha_voip',
                  'numero_telefone_voip'
               ]

class ReservarNumeroVoipForm(forms.ModelForm):
    class Meta:
        model = ServicoVoip
        fields = ['nome_usuario_voip',
                  'cpf_usuario_voip',
               ]


class FinalizarNumeroVoipForm(forms.ModelForm):
    class Meta:
        model = ServicoVoip
        fields = ['finalizado_voip']



