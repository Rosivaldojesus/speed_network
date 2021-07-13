from django import forms
from .models import TerminaisOpticos, CaixasDeEmenda


class CtoForm(forms.ModelForm):
    class Meta:
        model = TerminaisOpticos
        fields = ['codigo_cto',
         'rua_cto',
          'numero_rua_cto',
           'bairro',
            'pon_cto',
             'conexoes_opticas_cto',
              'board_cto',
               'quant_conexoes_usadas_cto',
                'observacao_cto']
        widgets = {

            #'observacao_instalacao' : forms.Textarea(attrs={'class': 'form control'})
        }

class InsertCtoForm(forms.ModelForm):
    class Meta:
        model = TerminaisOpticos
        fields = ['codigo_cto',
         'rua_cto',
          'numero_rua_cto',
           'bairro',
            'pon_cto',
             'conexoes_opticas_cto',
              'board_cto',
               'quant_conexoes_usadas_cto',
                'observacao_cto']
        widgets = {
            'codigo_cto': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'rua_cto': forms.TextInput(attrs={'class': 'form-control', 'required': True}),

        }


class CaixasDeEmendaForm(forms.ModelForm):
    class Meta:
        model = CaixasDeEmenda
        fields = ['codigo_caixa', 'rua_caixa_emenda', 'numero_rua_cto']
