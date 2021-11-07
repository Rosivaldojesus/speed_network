from django import forms
from .models import Instalacao, ValeRefeicao, Cancelamentos
from ..services.models import ServicoVoip
from ..components.models import FuncionariosParaVale, Bancos
from django.forms.widgets import NumberInput
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
                  'instalacao_vendedor',
                  'como_conheceu_empresa',
                  'observacao_instalacao',
                  ]
        widgets = {
            'nome_cliente': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'sobrenome_cliente': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'cpf_cliente': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'rg_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'rua_cliente': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'cep_cliente': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'numero_endereco_cliente': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'complemento_endereco_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro_cliente': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'cidade': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'telefone1_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone2_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'email_cliente': forms.EmailInput(attrs={'class': 'form-control'}),
            'planos_instalacao': forms.Select(attrs={'class': 'form-control'}),
            'data_vencimento': forms.Select(attrs={'class': 'form-control'}),
            'data_instalacao': forms.DateInput(attrs={'type': 'date'}),
            'hora_instalacao': forms.TimeInput(attrs={'type': 'time'}),
            'instalacao_vendedor': forms.Select(attrs={'class': 'form-control'}),
            'como_conheceu_empresa': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'observacao_instalacao' : forms.Textarea(attrs={'class': 'form-control'}),
        }

    COMO_CONHECEU_EMPRESA = (
        ('Panfleto', 'Panfleto'),
        ('Indicação', 'Indicação'),
        ('Site', 'Site'),
        ('Redes Socias', 'Redes Socias'),
        ('Outros', 'Outros'),
    )
    como_conheceu_empresa = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                        choices=COMO_CONHECEU_EMPRESA, required=True)



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
    data_instalacao = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    hora_instalacao = forms.TimeField(widget=forms.DateInput(attrs={"type": "time"}))
    status_agendada = forms.BooleanField(label='Marque para agendar instalação.')


class InstalacaoDefinirTecnicoForm(forms.ModelForm):
    class Meta:
        model = Instalacao

        fields = [
                  'funcionario_instalacao',
                  ]


class InstalacaoFinalizarForm(forms.ModelForm):
    class Meta:
        model = Instalacao
        fields = [
            'concluido',
            'material_utilizado',
            'data_finalizacao',

            'observacao_instalacao',
                  ]
        widgets = {
            'data_instalacao': forms.DateInput(attrs={'type': 'date'}),
            'hora_instalacao': forms.TimeInput(attrs={'type': 'time'}),
            'data_concluido': forms.DateInput(attrs={'type': 'date'}),
            'data_finalizacao': forms.DateInput(attrs={'type': 'date'}),

        }
    data_finalizacao = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    concluido = forms.BooleanField(label='Marque para finalizar instalação.')




class BoletoEntregueForm(forms.ModelForm):
    class Meta:
        model = Instalacao
        fields = ['boleto_entregue']
    boleto_entregue = forms.BooleanField(label='Marque para finalizar boleto.')

#------------------------------ VOIP -------------------------------------------------
class BoletoVoipEntregueForm(forms.ModelForm):
    class Meta:
        model = ServicoVoip
        fields = ['boleto_entregue']
    boleto_entregue = forms.BooleanField(label='Marque para finalizar boleto.')

    
#---------------------------------------------------------------------------------------

class EmitirValeRefeicaoForm(forms.ModelForm):
    class Meta:
        model = ValeRefeicao
        fields = ['nome_funcionario','data_vale']
        widgets = {

            'data_vale': forms.DateInput(attrs={'type': 'date'}),
        }
    nome_funcionario = forms.ModelChoiceField(queryset=FuncionariosParaVale.objects.all().order_by('nome_funcionario'))
    data_vale = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    #valor_vale = forms.DecimalField(required=False)



class AdicionarValorValeRefeicaoForm(forms.ModelForm):
    class Meta:
        model = ValeRefeicao
        fields = ['valor_vale']
    valor_vale = forms.DecimalField(required=True)


class AdicionarPagamentoValeRefeicaoForm(forms.ModelForm):
    class Meta:
        model = ValeRefeicao
        fields = ['status_pago']
    status_pago = forms.BooleanField()




# -------------- Cancellatios -------------------
class CadastrarCancelamentosForm(forms.ModelForm):
    class Meta:
        required_css_class = 'required'
        model = Cancelamentos
        fields = ['nome','cpf','endereco','numero' ,'cep','bairro','plano_internet','motivo','data' ]

    nome = forms.CharField()

    cpf = forms.CharField(widget=forms.TextInput, label='CPF:', required=True)
    endereco = forms.CharField(widget=forms.TextInput, label='Endereço:', required=True)
    numero = forms.CharField(widget=forms.TextInput, label='Nº:', required=True)
    cep = forms.CharField(widget=forms.TextInput, label='CEP:', required=True)
    bairro = forms.CharField(widget=forms.TextInput, label='Bairro:', required=True)

    PLANO_INTERNET = (
        ('69,90', '69,90'),
        ('89,90', '89,90'),
        ('99,90', '99,90'),
        ('119,90', '119,90'),
        ('149,90', '149,90'),
        ('Voip', 'Voip'),
    )
    plano_internet = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=PLANO_INTERNET)
    motivo = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}), label='Motivo do cancelamento:', required=True)
    data = forms.DateField(widget = forms.DateInput(attrs={"type": "date"}), label='Informe a data do cancelamento:')

    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get("nome")
        cpf = cleaned_data.get("cpf")
        if not (nome or cpf):
            raise forms.ValidationError(
                "You must enter either a phone number or an email, or both."
            )


class EditarCancelamentosForm(forms.ModelForm):
    class Meta:
        required_css_class = 'required'
        model = Cancelamentos
        fields = ['nome', 'cpf', 'endereco', 'numero', 'cep', 'bairro', 'plano_internet', 'motivo', 'data']

    nome = forms.CharField()

    cpf = forms.CharField(widget=forms.TextInput, label='CPF:', required=True)
    endereco = forms.CharField(widget=forms.TextInput, label='Endereço:', required=True)
    numero = forms.CharField(widget=forms.TextInput, label='Nº:', required=True)
    cep = forms.CharField(widget=forms.TextInput, label='CEP:', required=True)
    bairro = forms.CharField(widget=forms.TextInput, label='Bairro:', required=True)

    PLANO_INTERNET = (
        ('69,90', '69,90'),
        ('89,90', '89,90'),
        ('99,90', '99,90'),
        ('119,90', '119,90'),
        ('149,90', '149,90'),
        ('Voip', 'Voip'),
    )
    plano_internet = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                               choices=PLANO_INTERNET)
    motivo = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}), label='Motivo do cancelamento:',
                             required=True)
    #data = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), label='Informe a data do cancelamento:')
