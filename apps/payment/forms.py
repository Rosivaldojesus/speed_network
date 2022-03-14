from django import forms
from ..components.models import Bancos
from .models import Pagamento, FluxoEntradasSaidas, MeiosEntregaBoletos, TipoCusto, OrigemValores
from .models import DestinoValoresBoletos
from .models import ClientesEntregaBoletos


class CadastarPagamentoForm(forms.ModelForm):
    motivo_pagamento = forms.CharField(
        label='Motivo desse pagamento',
        help_text=(
            '- informe para onde vai esse pagamento'
        ),
        error_messages={
            'required': "Please Enter your Name",
            'min_lenght': 'Nome curto',
        }, required=False
    )

    valor_pagamento = forms.CharField(
        label='Valor a ser pago R$:',
        error_messages={
            'required': 'Qual é valor'
        }
    )

    data_pagamento = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Pagamento
        fields = [
            'motivo_pagamento', 'valor_pagamento', 'origem_valor_pagamento',
            'tipo_custo_pagamento', 'data_pagamento', 'categoria',
        ]

    # method for cleaning the data
    def clean(self):
        super(CadastarPagamentoForm, self).clean()

        # getting username and password from cleaned_data
        motivo_pagamento = self.cleaned_data.get('motivo_pagamento')
        valor_pagamento = self.cleaned_data.get('valor_pagamento')

        # validating the username and password
        if len(motivo_pagamento) < 4:
            self._errors['motivo_pagamento'] = self.error_class(['A minimum of 4 characters is required'])

        if len(motivo_pagamento) < 1:
            self._errors['valor_pagamento'] = self.error_class(['Informe o valor'])

        return self.cleaned_data


class EditarPagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = [
            'motivo_pagamento', 'valor_pagamento', 'informacao_pagamento', 'origem_valor_pagamento',
            'tipo_custo_pagamento', 'data_pagamento', 'categoria',
        ]


class AgendarPagamentoForm(forms.ModelForm):
    motivo_pagamento = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ex: Boleto do link'}),
    )
    valor_pagamento = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ex: 385,50'}),

    )
    informacao_pagamento = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Código de barras, Conta bancária, Chave PIX'}),
        label='Informações para pagamento',
        help_text='Caso haja código de barras, conta bancária, Chave Pix e etc',
        required=False
    )
    origem_valor_pagamento = forms.ModelChoiceField(
        queryset=OrigemValores.objects.all(),
        help_text='Origem do dinheiro Ex: Banco NET.'
    )
    tipo_custo_pagamento = forms.ModelChoiceField(
        queryset=TipoCusto.objects.all(),
        help_text='Referente a recorrência deste custo.'
    )
    data_pagamento = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Pagamento

        fields = [
            'motivo_pagamento', 'valor_pagamento', 'informacao_pagamento', 'origem_valor_pagamento',
            'tipo_custo_pagamento', 'data_pagamento', 'categoria',
        ]

    def clean(self):
        super(AgendarPagamentoForm, self).clean()

        # getting username and password from cleaned_data
        motivo_pagamento = self.cleaned_data.get('motivo_pagamento')

        # validating the username and password
        if len(motivo_pagamento) < 4:
            self._errors['motivo_pagamento'] = self.error_class(['Descreva melhor o gasto.'])

        return self.cleaned_data


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
            'nome_cliente', 'cpf_cliente', 'boleto_assinado', 'forma_entrega',
        ]
    nome_cliente = forms.CharField()
    cpf_cliente = forms.CharField()
    # forma_entrega = forms.BooleanField()
    forma_entrega = forms.ModelChoiceField(queryset=MeiosEntregaBoletos.objects.all())
