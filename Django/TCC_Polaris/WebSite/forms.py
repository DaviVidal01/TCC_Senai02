from django import forms
from django.shortcuts import render
from .models import Fotos_BD, Comentarios_BD, Like_BD, Barra_Pesquisa
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

class RegisterForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'custom-input'})),
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'custom-input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'custom-input'}),
            'email': forms.TextInput(attrs={'class': 'custom-input'}),
            'password': forms.PasswordInput(attrs={'class': 'custom-input'}),
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
    