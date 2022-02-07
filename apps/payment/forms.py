from django import forms
from ..components.models import Bancos
from .models import Pagamento, FluxoEntradasSaidas, MeiosEntregaBoletos
from .models import DestinoValoresBoletos
from .models import ClientesEntregaBoletos


class CadastarPagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = [
            'motivo_pagamento',
            'valor_pagamento',
            'origem_valor_pagamento',
            'tipo_custo_pagamento',
            'data_pagamento',
            'categoria',
            'status_pago',
        ]
    data_pagamento = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    status_pago = forms.BooleanField(required=True, initial=True, label='Confirmar pagamento')


class EditarPagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = [
            'motivo_pagamento',
            'valor_pagamento',
            'origem_valor_pagamento',
            'tipo_custo_pagamento',
            'data_pagamento',
            'categoria',
        ]
 

class AgendarPagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = [
            'motivo_pagamento',
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
        fields = [
            'status_pago'
        ]
    status_pago = forms.BooleanField(required=True, initial=False, label='Marque aqui, para confirmar pagamento')


class CadastrarFluxoForm(forms.ModelForm):
    class Meta:
        model = FluxoEntradasSaidas
        fields = [
            'fluxo_data', 'banco', 'saldoInicial', 'entradaDia',  'SaidaDia', 'SaldoDia'
        ]
    saldoInicial = forms.DecimalField(label='Saldo do início do dia R$:')
    entradaDia = forms.DecimalField(label='Total de entradas do dia R$:')
    fluxo_data = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), required=False)
    SaidaDia = forms.DecimalField(label='Total de saídas do dia R$:')
    SaldoDia = forms.DecimalField(label='Saldo do final do dia R$:')


class CadastarDestinoValoresBoletosForm(forms.ModelForm):
    class Meta:
        model = DestinoValoresBoletos
        fields = [
            'valor', 'destino', 'data_transacao'
        ]
    valor = forms.DecimalField(label="Valor transferido")
    destino = forms.ModelChoiceField(queryset=Bancos.objects.all().order_by('nome_banco'), label="Banco de destino")
    data_transacao = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), label="Data da transação")


class EditarDestinoValoresBoletosForm(forms.ModelForm):
    class Meta:
        model = DestinoValoresBoletos
        fields = [
            'valor', 'destino', 'data_transacao'
        ]
    valor = forms.DecimalField(label="Valor transferido")
    destino = forms.ModelChoiceField(queryset=Bancos.objects.all().order_by('nome_banco'), label="Banco de destino")


class ClientesEntregaBoletosForm(forms.ModelForm):
    class Meta:
        model = ClientesEntregaBoletos
        fields = [
            'nome_cliente', 'cpf_cliente', 'forma_entrega'
        ]
        nome_cliente = forms.CharField(label='Group', help_text='Some text')
        exclude = ['', ]

    def clean(self):
        super(ClientesEntregaBoletosForm, self).clean()

        nome_cliente = self.cleaned_data.get('nome_cliente')
        cpf_cliente = self.cleaned_data.get('cpf_cliente')
        forma_entrega = self.cleaned_data.get('forma_entrega')

        if not nome_cliente:
            self._errors['nome_cliente'] = self.error_class(['Informe o nome do cliente'])
         
        if not cpf_cliente:
            self._errors['cpf_cliente'] = self.error_class(['Preencha o cpf do cliente'])

        if not forma_entrega:
            self._errors['forma_entrega'] = self.error_class(['Informe como o boleto foi entregue ao cliente'])

        return self.cleaned_data


class EditarClientesEntregaBoletosForm(forms.ModelForm):
    class Meta:
        model = ClientesEntregaBoletos
        fields = [
            'nome_cliente',
            'cpf_cliente',
            'boleto_assinado',
            'forma_entrega',
        ]
    nome_cliente = forms.CharField()
    cpf_cliente = forms.CharField()
    forma_entrega = forms.BooleanField()
    forma_entrega = forms.ModelChoiceField(queryset=MeiosEntregaBoletos.objects.all())
