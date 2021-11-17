from django import forms
from django.db import models
from django.forms import fields
from ..components.models import Bancos
from django.core.exceptions import ValidationError

from .models import Pagamento, AgendaPagamento, FluxoEntradasSaidas, DestinoValoresBoletos
from .models import DestinoValoresBoletos
from .models import ClientesEntregaBoletos





class CadastarPagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields =['motivo_pagamento',
                 'valor_pagamento',
                 'origem_valor_pagamento',
                 'tipo_custo_pagamento',
                 'data_pagamento',
                 'categoria',
                 'status_pago',
                 ]
    data_pagamento = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    status_pago = forms.BooleanField(required=True, initial=True, label='Comfirmar pagamento')


class EditarPagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields =['motivo_pagamento',
                 'valor_pagamento',
                 'origem_valor_pagamento',
                 'tipo_custo_pagamento',
                 'data_pagamento',
                 'categoria',
                 'status_pago',
                 ]
    status_pago = forms.BooleanField(required=True, initial=True, label='Comfirmar pagamento')


class AgendarPagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields =['motivo_pagamento',
                 'valor_pagamento',
                 'origem_valor_pagamento',
                 'tipo_custo_pagamento',
                 'data_pagamento',
                 'categoria',
                 ]

    data_pagamento = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))



'''
class AgendarPagamentoForm(forms.ModelForm):
    class Meta:
        model = AgendaPagamento
        fields = ['data_pagamento',]
    data_pagamento = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
'''

class ComfirmarPagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['status_pago']

    status_pago = forms.BooleanField(required=True, initial=False, label='Comfirmar pagamento')



class CadastrarFluxoForm(forms.ModelForm):
    class Meta:
        model = FluxoEntradasSaidas
        fields = ['fluxo_data','banco', 'saldoInicial','entradaDia',  'SaidaDia', 'SaldoDia']

    saldoInicial = forms.DecimalField(label='Saldo do início do dia R$:')
    entradaDia = forms.DecimalField(label='Total de entradas do dia R$:')
    fluxo_data = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), required=False)
    SaidaDia = forms.DecimalField(label='Total de saídas do dia R$:')
    SaldoDia = forms.DecimalField(label='Saldo do final do dia R$:')


class CadastarDestinoValoresBoletosForm(forms.ModelForm):
    class Meta:
        model = DestinoValoresBoletos
        fields = ['valor', 'destino', 'data_transacao']

    valor = forms.DecimalField(label="Valor transferido")
    destino = forms.ModelChoiceField(queryset=Bancos.objects.all().order_by('nome_banco'), label="Banco de destino")
    data_transacao = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), label="Data da transação")



class EditarDestinoValoresBoletosForm(forms.ModelForm):
    class Meta:
        model = DestinoValoresBoletos
        fields = ['valor', 'destino', 'data_transacao']

    valor = forms.DecimalField(label="Valor transferido")
    destino = forms.ModelChoiceField(queryset=Bancos.objects.all().order_by('nome_banco'), label="Banco de destino")
    #data_transacao = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), label="Data da transação")


class ClientesEntregaBoletosForm(forms.ModelForm):

    # meta data for displaying a form
    class Meta:
        # model
        model = ClientesEntregaBoletos

        # displaying fields
        filds= ['nome_cliente', 'cpf_cliente', 'data_transacao']

        #Exclude
        exclude = ['',]


    # method for cleaning the data
    def clean(self):
      super(ClientesEntregaBoletosForm, self).clean()

      # getting username and password from cleaned_data
      nome_cliente = self.cleaned_data.get('nome_cliente')
      cpf_cliente = self.cleaned_data.get('cpf_cliente')

      # validating the username and password
      if len(nome_cliente) > 50:
         self._errors['nome_cliente'] = self.error_class(['A minimum of 5 characters is required'])

      if len(cpf_cliente) > 80:
         self._errors['cpf_cliente'] = self.error_class(['Password length should not be less than 8 characters'])

      return self.cleaned_data


class EditarClientesEntregaBoletosForm(forms.ModelForm):

    # meta data for displaying a form
    class Meta:
        # model
        model = ClientesEntregaBoletos

        # displaying fields
        filds= ['nome_cliente', 'cpf_cliente','forma_entrega', 'data_transacao']

        #Exclude
        exclude = ['',]




