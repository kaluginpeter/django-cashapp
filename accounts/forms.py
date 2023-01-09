# dappx/forms.py
from django import forms
from accounts.models import UserProfileInfo
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core import validators
import django.contrib.auth.password_validation


class UserForm(forms.ModelForm):
    error_css_class = 'alert'
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               validators=[validate_password], label='Пароль')

    class Meta():
        model = User
        fields = ('username', 'password', 'email')
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'})}
