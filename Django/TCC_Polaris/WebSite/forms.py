from django import forms
from django.shortcuts import render
from .models import Produtos_BD, Barra_Pesquisa, Tecido_BD, Tipo_BD, Marca_BD, Tamanho_BD
from django import forms
from django.contrib.auth.models import User

class LoginForms(forms.Form):
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'type': "email",
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
            }
        ),
    )

class RegisterForms(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
            }
        )),
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
            }
        ))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(),
            'email': forms.TextInput(),
            'password': forms.PasswordInput(),
        }

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Senhas não são iguais')

        return password_confirm

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_staff = 1
        if commit:
            user.save()
        return user

class ProdutosForms(forms.ModelForm):
    class Meta:
        model = Produtos_BD
        fields = ['titulo', 'descricao', 'foto', 'preco', 'genero', 'tecido', 'tamanho', 'tipo', 'marca']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'custom-input'}),
            'descricao': forms.Textarea(attrs={'class': 'custom-textarea'}),
            'foto': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'preco': forms.NumberInput(attrs={'class': 'custom-input'}),
            'genero': forms.Select(attrs={'class': 'custom-input'}),
            'tecido': forms.Select(attrs={'class': 'custom-input'}),
            'tamanho': forms.Select(attrs={'class': 'custom-input'}),
            'tipo': forms.Select(attrs={'class': 'custom-input'}),
            'marca': forms.Select(attrs={'class': 'custom-input'}),
        }

class Barra_Pesquisa(forms.ModelForm):
    class Meta:
        model = Barra_Pesquisa
        fields = ['imagem']
        widgets = {
            'imagem': forms.FileInput(attrs={'class': 'custom-file-input'}),
        }
    