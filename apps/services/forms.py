from django import forms
from .models import Servico, ServicoVoip
from ..components.models import PlanosInternet
from ..services.models import CategoriaServico

class ServicoForm(forms.ModelForm):

    contato_servico = forms.CharField(label='Nome do cliente.')
    plano_internet = forms.ModelChoiceField(
        queryset=PlanosInternet.objects.all(), required=True,label='Qual o plano do cliente?')
    endereco_servico = forms.CharField(
        required=False, widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}),label='Endereço do serviço.')
    servico_para_executar = forms.CharField(
        required=False, widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}),label='Serviço a fazer.')
    categoria = forms.ModelChoiceField(queryset=CategoriaServico.objects.all(), label='Tipo de serviço.')

    class Meta:
        model = Servico
        fields = [
            'contato_servico', 'plano_internet', 'endereco_servico', 'servico_para_executar', 'categoria'
        ]
    
class AgendarServicoForm(forms.ModelForm):

    data_agendada = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    hora_agendada = forms.TimeField(widget=forms.DateInput(attrs={"type": "time"}))

    class Meta:
        model = Servico
        fields = [
            'data_agendada', 'hora_agendada'
        ]

class EditarAgendarServicoForm(forms.ModelForm):

    data_agendada = forms.DateField(
        label='Data do serviço',
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={'type': 'date'}
        )
    )
    hora_agendada = forms.TimeField(
        widget=forms.TimeInput(
            format='%H:%M',
            attrs={'type': 'time'}
        )
    )
    categoria = forms.ModelChoiceField(queryset=CategoriaServico.objects.all())
    servico_para_executar = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}),label='Serviço a fazer')

    status_analise = forms.BooleanField(
        required=False,
        label='Enviar para análise.'
    )
    observacao = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}),label='Observações', required=False)

    class Meta:
        model = Servico
        fields = [
            'contato_servico','status_agendado', 'servico_para_executar', 'data_agendada',
             'hora_agendada', 'categoria', 'status_analise', 'observacao'
        ]

    
class FinalizarServicoForm(forms.ModelForm):

    status_concluido = forms.BooleanField(label='Marque para finalizar.')
    data_finalizacao = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    
    class Meta:
        model = Servico
        fields = [
            'servico_executado', 'material_utilizado', 'data_finalizacao', 'status_concluido'
        ]
        widgets = {
            'data_finalizacao': forms.DateInput(attrs={'type': 'date'}),
            'hora_agendada': forms.TimeInput(attrs={'type': 'time'}),
        }
    

class ReservarVoipForm(forms.ModelForm):

    reservado_voip = forms.BooleanField(label='Marque para reservar.')

    class Meta:
        model = ServicoVoip
        fields = [
            'nome_usuario_voip', 'cpf_usuario_voip', 'reservado_voip'
        ]
    

class ReservarVoipPortabilidadeForm(forms.ModelForm):
    class Meta:
        model = ServicoVoip
        fields = [
            'nome_usuario_voip', 'cpf_usuario_voip', 'reservado_voip', 'portabilidade_voip'
        ]
