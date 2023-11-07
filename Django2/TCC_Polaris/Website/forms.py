from django import forms
from django.shortcuts import render
from .models import Fotos_BD, Comentarios_BD, Like_BD, Barra_Pesquisa

class LoginForms(forms.Form):
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'type': "email",
                'class': 'form-control px-4 rounded-pill OrageBorder',
                'placeholder': 'Ex.: jose@django.com',
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
                'class': 'form-control px-4 rounded-pill OrageBorder',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )

class RegisterForms(forms.Form):
    name = forms.CharField(
        label='Nome de Cadastro', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control px-4 rounded-pill OrageBorder',
                'placeholder': 'Ex.: João da Silva',
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'type': "email",
                'class': 'form-control px-4 rounded-pill OrageBorder',
                'placeholder': 'Ex.: jose@django.com',
            }
        )
    )
    password = forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'class': 'form-control px-4 rounded-pill OrageBorder',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )
    password_confirm = forms.CharField(
        label='Confirme a sua senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'class': 'form-control px-4 rounded-pill OrageBorder',
                'placeholder': 'Digite a sua senha novamente',
            }
        ),
    )

def clean_name(self):
    name = self.cleaned_data.get('name')

    if name and ' ' in name:
        raise forms.ValidationError('Espaços não são permitidos nesse campo')

    return name

def clean_password_confirm(self):
    password = self.cleaned_data.get('password')
    password_confirm = self.cleaned_data.get('password_confirm')

    if password and password_confirm and password != password_confirm:
        raise forms.ValidationError('Senhas não são iguais')

    return password_confirm

class FotoForms(forms.ModelForm):
    class Meta:
        model = Fotos_BD
        fields = ['titulo', 'descricao', 'foto']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'custom-input'}),
            'descricao': forms.Textarea(attrs={'class': 'custom-textarea'}),
            'foto': forms.FileInput(attrs={'class': 'custom-file-input'}),
        }
    
class ComentarioForms(forms.ModelForm):
    class Meta:
        model = Comentarios_BD
        fields = ['comentario', 'data_comentario', 'autor']

class LikeForms(forms.ModelForm):
    class Meta:
        model = Like_BD
        fields = ['like', 'autor']

class Barra_Pesquisa(forms.ModelForm):
    class Meta:
        model = Barra_Pesquisa
        fields = ['imagem']
        widgets = {
            'imagem': forms.FileInput(attrs={'class': 'custom-file-input'}),
        }
    