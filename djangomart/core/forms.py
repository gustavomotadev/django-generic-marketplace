from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

_custom_input_class = 'w-full py-4 px-6 rounded-xl'

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': _custom_input_class
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your E-mail Address',
        'class': _custom_input_class
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'A Strong Password',
        'class': _custom_input_class
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat Your Password',
        'class': _custom_input_class
    }))

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': _custom_input_class
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': _custom_input_class
    }))
