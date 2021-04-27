from django import forms
from .models import Instalacao

class InstalacaoForm(forms.ModelForm):
    class Meta:
        model = Instalacao
        fields = ['nome_cliente',
                  'cpf_cliente',
                  'rg_cliente',
                  'rua_cliente',
                  'cep_cliente',
                  'bairro_cliente',
                  'numero_endereco_cliente',
                  'complemento_endereco_cliente',
                  'cidade',
                  'telefone_cliente',
                  'email_cliente',
                  'planos_instalacao']