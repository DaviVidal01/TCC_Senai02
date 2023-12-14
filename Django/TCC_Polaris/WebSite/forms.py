from django import forms
from django.shortcuts import render
from .models import Produtos_BD, Pedido_BD, Barra_Pesquisa, Tecido_BD, Tipo_BD, Marca_BD, Tamanho_BD
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

class UserForms(forms.ModelForm):
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

class RegisterForms(forms.Form):
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(attrs={'type': 'email'}),
    )
    username = forms.CharField(
        label='Username',
        required=True,
        max_length=30,
        widget=forms.TextInput(attrs={'type': 'text'}),
    )
    password = forms.CharField(
        label='Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(attrs={'type': 'password'}),
    )
    password_confirm = forms.CharField(
        label='Confirmar Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(attrs={'type': 'password'}),
    )


    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Senhas não são iguais')

        return password_confirm
        
class ProdutosForms(forms.ModelForm):
    class Meta:
        model = Produtos_BD
        fields = ['titulo', 'descricao', 'foto', 'preco', 'genero', 'tecido', 'tamanho', 'tipo', 'marca']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'custom-input'}),
            'foto': forms.FileInput(attrs={'class': 'custom-input'}),
            'descricao': forms.Textarea(attrs={'class': 'custom-textarea'}),
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
    
class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Pedido_BD
        fields = ['nome', 'sobrenome', 'email', 'endereco_entrega', 'quantidade', 'pais', 'estado', 'cep']
        widgets = {
            'nome': forms.TextInput(attrs={'type':"text", 'class':"form-control", 'id':"firstName", 'placeholder':"", 'value':"", 'required':'True'}),
            'sobrenome': forms.TextInput(attrs={'type':"text", 'class':"form-control", 'id':"lastName", 'placeholder':"", 'value':"", 'required':'True'}),
            'email': forms.TextInput(attrs={'type':"email", 'class':"form-control", 'id':"email", 'placeholder':"email@email.com", 'required':'True'}),
            'endereco': forms.TextInput(attrs={'type':"text", 'class':"form-control", 'id':"address", 'placeholder':"Rua X, 123, Bairro Y", 'required':'True'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control quantidade-input', 'type':'number', 'value':'0'}),
            'pais': forms.Select(attrs={'class': 'custom-select d-block w-100', 'id':'country', 'placeholder':"Selecione Aqui", 'required':'True'}),
            'estado': forms.Select(attrs={'class': 'custom-select d-block w-100', 'id':'state', 'placeholder':"Selecione Aqui", 'required':'True'}),
            'cep': forms.TextInput(attrs={'type':"text", 'class':"form-control", 'id':"zip", 'placeholder':"00000-000", 'value':"", 'required':'True'}),
        }