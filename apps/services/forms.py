
from django import forms
from django.contrib.auth.models import User
from .models import Servico


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['contato_servico',
                  'endereco_servico',
                  'servico_para_executar',
                  'categoria',]
        widgets = {
            'data_agendada': forms.DateInput(attrs={'type': 'date'}),
            'hora_agendada': forms.TimeInput(attrs={'type': 'time'}),
        }


class AgendarServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['status_agendado','data_agendada', 'hora_agendada',]
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
        fields = ['status_agendado','servico_para_executar','data_agendada', 'hora_agendada']
        widgets = {
            'data_agendada': forms.DateInput(attrs={'type': 'date'}),
            'hora_agendada': forms.TimeInput(attrs={'type': 'time'}),
            'data_finalizacao': forms.DateInput(attrs={'type': 'date'}),
            'hora_instalacao': forms.TimeInput(attrs={'type': 'time'}),
        }




class FinalizarServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['servico_executado',
                  'material_utilizado',
                  'data_finalizacao',
                  'status_concluido',
                  ]
        widgets = {
            'data_finalizacao': forms.DateInput(attrs={'type': 'date'}),
            'hora_agendada': forms.TimeInput(attrs={'type': 'time'}),
        }

    status_concluido = forms.BooleanField(label='Marque para finalizar.')
    data_finalizacao = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )










    def clean_status_agendada(self):
        agendado = self.clean_status_agendada('agendado')
        if agendado == False:
            raise forms.ValidationError('Preencher o campo data')
        return agendado







