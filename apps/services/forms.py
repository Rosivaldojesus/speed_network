
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
    data_agendada = forms.DateInput()


    def clean_status_agendada(self):
        agendado = self.clean_status_agendada('agendado')
        if agendado == False:
            raise forms.ValidationError('Preencher o campo data')
        return agendado






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
                  'status_concluido',]
        widgets = {
            'data_finalizacao': forms.DateInput(attrs={'type': 'date'}),
            'hora_agendada': forms.TimeInput(attrs={'type': 'time'}),
        }

    funcionario_instalacao = forms.ModelChoiceField(
        queryset=User.objects.filter(id__in=['2','12', '13', '14']),

        label='Funcionário serviço',
        widget=forms.Select
    )

    data_finalizacao = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )


    status_concluido = forms.BooleanField(label='Marque aqui para finalizar.'),



    def clean_status_agendada(self):
        agendado = self.clean_status_agendada('agendado')
        if agendado == False:
            raise forms.ValidationError('Preencher o campo data')
        return agendado







