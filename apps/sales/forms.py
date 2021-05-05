from django import forms
from .models import Instalacao


class InstalacaoCreateForm(forms.ModelForm):
    class Meta:
        model = Instalacao
        fields = ['nome_cliente',
                  'sobrenome_cliente',



                  'rua_cliente',
                  'numero_endereco_cliente',
                  'complemento_endereco_cliente',
                  'bairro_cliente',
                  'cidade',


                  'telefone_cliente',
                  'email_cliente',


                  'planos_instalacao',
                  'data_vencimento']
        widgets = {
            'nome_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'sobrenome_cliente': forms.TextInput(attrs={'class': 'form-control'}),



            'rua_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_endereco_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento_endereco_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.Select(attrs={'class': 'form-control'}),



            'telefone_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'email_cliente': forms.EmailInput(attrs={'class': 'form-control'}),


            'planos_instalacao': forms.Select(attrs={'class': 'form-control'}),
            'data_vencimento': forms.Select(attrs={'class': 'form-control'}),

            'data_instalacao': forms.DateInput(attrs={'type': 'date'}),
            'hora_instalacao': forms.TimeInput(attrs={'type': 'time'}),
        }

class InstalacaoUpdateForm(forms.ModelForm):
    class Meta:
        model = Instalacao
        fields = ['nome_cliente',
                  'sobrenome_cliente',
                  'cpf_cliente',
                  'rg_cliente',
                  'cep_cliente',
                  'rua_cliente',
                  'bairro_cliente',
                  'numero_endereco_cliente',
                  'complemento_endereco_cliente',
                  'cidade',
                  'telefone_cliente',
                  'email_cliente',
                  'planos_instalacao',
                  'data_vencimento',
                  'data_instalacao',
                  'hora_instalacao',
                  'observacao_instalacao',
                  ]
        data_instalacao = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget)






'''
class InstalacaoForm(forms.ModelForm):
    class Meta:
        model = Instalacao
        fields = "__all__"
        date_time = forms.DateTimeField(initial=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), required=False)
        widgets = {

            'data_instalacao': forms.DateTimeField(attrs={'type': 'date'}),
            'hora_instalacao': forms.DateTimeField(attrs={'type': 'time'}),
        }
        '''





