import re

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.password_validation import validate_password
from .models import SenhasPorEquipamentos
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class UserForm(forms.ModelForm):
    password = forms.CharField(validators=[
        RegexValidator('(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$',
                       message="A senha deverá ter no minímo 8 digitos e  caracteres Ex.: $%#@*&%...")])

    email = forms.CharField(validators=[
        RegexValidator('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
                       message="Digite um email válido Ex.: example@example.com")])

    class Meta:
        model = User

        fields = ['first_name', 'last_name', 'username', 'password','email']
        """
        first_name = forms.CharField(label='Primeiro snome', max_length=100, widget=forms.TextInput(
            attrs={'class': "input"})
                                 )
        """
    def first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if User.objects.filter(first_name=first_name).exists():
            raise forms.ValidationError('Esse nome já existe.')
        return first_name

    def clean_password(self):
        password = self.cleaned_data['password']

        if len(password) < 8:
            self._errors['password'] = self.error_class(['A senha é muito curta'])

        return password

    def clean(self):
        super(UserForm, self).clean()
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        username = self.cleaned_data.get('username')

        if first_name == username:
            self._errors['username'] = self.error_class(['O usuário não pode ser igual ao nome'])

        if not first_name:
            self._errors['first_name'] = self.error_class(['Informe o nome do cliente'])

        if not last_name:
            self._errors['last_name'] = self.error_class(['Informe sobrenome'])

        if not username:
            self._errors['username'] = self.error_class(['Informe um nome de usuário'])

        return self.cleaned_data


    def clean_email(self):
        email = self.cleaned_data['email']
        validator = RegexValidator(
            "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")
        validator(email)

        return email




'''
    def clean(self):
        cleaned_data = super().clean()

        nome = self.cleaned_data.get('first_name')
        sobrenome = self.cleaned_data.get('last_name')

        if nome == sobrenome:
            raise forms.ValidationError('Preencha o nome')
        return cleaned_data
'''

class SenhasPorEquipamentosForm(forms.ModelForm):
    class Meta:
        model = SenhasPorEquipamentos
        fields = [
            'codigo_equipamento', 'sn_equipamento', 'equipamento', 'ip_equipamento', 'login', 'senha',
            'fabricante', 'patrimonio_equipamento'
        ]
