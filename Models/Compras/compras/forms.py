from django import forms
from django.contrib.auth.models import User
from .models import Produto, Pedido

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco']

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nome', 'sobrenome', 'email_cliente', 'endereco_entrega', 'quantidade']


# USER **
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
