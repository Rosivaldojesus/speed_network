from django import forms
from .models import Instalacao


class InstalacaoForm(forms.ModelForm):
    class Meta:
        model = Instalacao
        fields = "__all__"

        widgets = {
            'data_instalacao': forms.DateTimeInput(attrs={'type': 'date'}),
            'hora_instalacao': forms.DateTimeInput(attrs={'type': 'time'}),
        }






