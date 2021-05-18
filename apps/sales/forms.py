from django import forms
from .models import Instalacao
from django.contrib.auth.models import User



class InstalacaoCreateForm(forms.ModelForm):
    class Meta:
        model = Instalacao
        fields = ['nome_cliente',
                  'sobrenome_cliente',
                  'cpf_cliente',
                  'rua_cliente',
                  'cep_cliente',
                  'numero_endereco_cliente',
                  'complemento_endereco_cliente',
                  'bairro_cliente',
                  'cidade',
                  'telefone1_cliente',
                  'telefone2_cliente',
                  'email_cliente',
                  'planos_instalacao',
                  'data_vencimento',
                  'observacao_instalacao',

                  ]
        widgets = {
            'nome_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'sobrenome_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'rg_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'rua_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'cep_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_endereco_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento_endereco_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.Select(attrs={'class': 'form-control'}),
            'telefone1_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone2_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'email_cliente': forms.EmailInput(attrs={'class': 'form-control'}),
            'planos_instalacao': forms.Select(attrs={'class': 'form-control'}),
            'data_vencimento': forms.Select(attrs={'class': 'form-control'}),
            'data_instalacao': forms.DateInput(attrs={'type': 'date'}),
            'hora_instalacao': forms.TimeInput(attrs={'type': 'time'}),
            'observacao_instalacao' : forms.Textarea(attrs={'class': 'form control'})
        }

class InstalacaoUpdateForm(forms.ModelForm):
    class Meta:
        model = Instalacao
        fields = ['nome_cliente',
                  'sobrenome_cliente',
                  'cpf_cliente',
                  'cep_cliente',
                  'rua_cliente',
                  'bairro_cliente',
                  'numero_endereco_cliente',
                  'complemento_endereco_cliente',
                  'cidade',
                  'email_cliente',
                  'telefone1_cliente',
                  'telefone2_cliente',
                  'planos_instalacao',
                  'data_vencimento',
                  'data_instalacao',
                  'hora_instalacao',
                  'observacao_instalacao',
                  ]
        data_instalacao = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget)






class InstalacaoAgendarForm(forms.ModelForm):
    class Meta:
        model = Instalacao

        fields = [
                  'status_agendada',
                  'data_instalacao',
                  'hora_instalacao',

                  ]

        widgets = {
            'data_instalacao': forms.DateInput(attrs={'type': 'date'}),
            'hora_instalacao': forms.TimeInput(attrs={'type': 'time'}),
        }
    status_agendada = forms.BooleanField(label='Marque para agendar instalação.')



class InstalacaoFinalizarForm(forms.ModelForm):
    class Meta:
        model = Instalacao
        fields = [
            'concluido',
            'material_utilizado',

            'data_finalizacao',
            'funcionario_instalacao',
            'observacao_instalacao',
                  ]
        widgets = {
            'data_instalacao': forms.DateInput(attrs={'type': 'date'}),
            'hora_instalacao': forms.TimeInput(attrs={'type': 'time'}),
            'data_concluido': forms.DateInput(attrs={'type': 'date'}),
            'data_finalizacao': forms.DateInput(attrs={'type': 'date'}),

        }
    funcionario_instalacao = forms.ModelChoiceField(
        queryset=User.objects.filter(id__in=['12','13','14']),

        label='Funcionário instalação',
        widget=forms.Select
    )
    data_finalizacao = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )
    concluido = forms.BooleanField(label='Marque para finalizar instalação.')






    










