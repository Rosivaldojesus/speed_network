from django import forms
from .models import TerminaisOpticos


class CtoForm(forms.ModelForm):
    class Meta:
        model = TerminaisOpticos
        fields = ['codigo_cto']
        widgets = {

            #'observacao_instalacao' : forms.Textarea(attrs={'class': 'form control'})
        }