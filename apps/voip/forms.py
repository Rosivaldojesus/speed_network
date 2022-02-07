from django import forms
from .models import ServicoVoip


class AdicionarNumeroVoipForm(forms.ModelForm):
    class Meta:
        model = ServicoVoip
        fields = [
            'usuario_voip',
            'senha_voip',
            'numero_telefone_voip'
        ]


class SolicitarPortabilidadeVoipForm(forms.ModelForm):
    class Meta:
        model = ServicoVoip
        fields = [
            'nome_usuario_voip',
            'cpf_usuario_voip',
            'numero_telefone_voip'
        ]


class SolicitarNumeroVoipForm(forms.ModelForm):
    class Meta:
        model = ServicoVoip
        fields = [
            'nome_usuario_voip',
            'cpf_usuario_voip',
            'observacao_voip'
        ]


class ReservarNumeroVoipForm(forms.ModelForm):
    class Meta:
        model = ServicoVoip
        fields = [
            'usuario_voip',
            'senha_voip',
            'numero_telefone_voip',
        ]


class FinalizarNumeroVoipForm(forms.ModelForm):
    class Meta:
        model = ServicoVoip
        fields = ['finalizado_voip']


#  Finaliza o Voip, que ainda não tiveram os beletos conferidos


class FinalizarNumeroVoipSemBoletoForm(forms.ModelForm):
    class Meta:
        model = ServicoVoip
        fields = [
            'boleto_entregue'
        ]


class PortabilidadeEnviarAnaliseForm(forms.ModelForm):
    class Meta:
        model = ServicoVoip
        fields = [
            'portabilidade_analise'
        ]
