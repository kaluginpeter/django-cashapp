# dappx/forms.py
from django import forms
from accounts.models import UserProfileInfo
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core import validators
import django.contrib.auth.password_validation

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,validators=[validate_password])
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')