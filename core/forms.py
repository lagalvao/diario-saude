# _*_ coding: utf-8 _*_
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Controle, Analise, Historico


class AuthenticationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )

    error_messages = {
        'invalid_login': (
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': ("This account is inactive."),
    }


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        #fields = '__all__' puxa todos os campos
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','placeholder': 'Crie um usuário', 'required':'required'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Informe seu email', 'required':'required'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Crie uma senha', 'required':'required'}),
        }

        error_messages = {
            'username':{
                'required': 'Este campo é obrigatorio'
            },
            'email': {
                'required': 'Este campo é obrigatorio'
            },
            'password': {
                'required': 'Este campo é obrigatorio'
            },
        }


    def save(self, commit=True):
        user = super(UserModelForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = '__all__' puxa todos os campos
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe um usuário'}),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Informe o primeiro nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe ultimo nome'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe seu email'}),
        }


class formControle(forms.ModelForm):
    class Meta:
        model = Controle
        fields = ['usuario', 'titulo', 'cor', 'data_inicio', 'data_fim']


class formAnalise(forms.ModelForm):
    class Meta:
        model = Analise
        fields = ['usuario', 'remedio']


class formHistorico(forms.ModelForm):
    class Meta:
        model = Historico
        fields = ['usuario', 'remedio']