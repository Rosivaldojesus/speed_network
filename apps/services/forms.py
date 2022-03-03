from django import forms
from django.forms import DateInput
from bootstrap_datepicker_plus import DatePickerInput
from .models import Servico, ServicoVoip
from ..components.models import PlanosInternet
from ..services.models import CategoriaServico


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = [
            'contato_servico', 'plano_internet', 'endereco_servico', 'servico_para_executar', 'categoria'
        ]
    contato_servico = forms.CharField(label='Nome do cliente.')
    plano_internet = forms.ModelChoiceField(queryset=PlanosInternet.objects.all(), required=True,
                                            label='Qual o plano do cliente?')
    endereco_servico = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}),
                                       label='Endereço do serviço.')
    servico_para_executar = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}),
                                            label='Serviço a fazer.')
    categoria = forms.ModelChoiceField(queryset=CategoriaServico.objects.all(), label='Tipo de serviço.')


class AgendarServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = [
            'status_agendado', 'data_agendada', 'hora_agendada'
        ]
        widgets = {
            'data_agendada': forms.DateInput(attrs={'type': 'date'}),
            'hora_agendada': forms.TimeInput(attrs={'type': 'time'}),
        }
    status_agendado = forms.BooleanField(label='Marque para agendar.')
    data_agendada = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    hora_agendada = forms.TimeField(widget=forms.DateInput(attrs={"type": "time"}))


class EditarAgendarServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = [
            'status_agendado', 'servico_para_executar', 'data_agendada', 'hora_agendada', 'categoria', 'status_analise'
        ]
        widgets = {
            'data_agendada': DatePickerInput(),
        }

    hora_agendada = forms.TimeField()
    categoria = forms.ModelChoiceField(queryset=CategoriaServico.objects.all())
    servico_para_executar = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}),
                                            label='Serviço a fazer'
                                            )


class FinalizarServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = [
            'servico_executado', 'material_utilizado', 'data_finalizacao', 'status_concluido'
        ]
        widgets = {
            'data_finalizacao': forms.DateInput(attrs={'type': 'date'}),
            'hora_agendada': forms.TimeInput(attrs={'type': 'time'}),
        }
    status_concluido = forms.BooleanField(label='Marque para finalizar.')
    data_finalizacao = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))


class ReservarVoipForm(forms.ModelForm):
    class Meta:
        model = ServicoVoip
        fields = [
            'nome_usuario_voip', 'cpf_usuario_voip', 'reservado_voip'
        ]
    reservado_voip = forms.BooleanField(label='Marque para reservar.')


class ReservarVoipPortabilidadeForm(forms.ModelForm):
    class Meta:
        model = ServicoVoip
        fields = [
            'nome_usuario_voip', 'cpf_usuario_voip', 'reservado_voip', 'portabilidade_voip'
        ]
