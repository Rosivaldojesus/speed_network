from django import forms
from .models import TerminaisOpticos


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