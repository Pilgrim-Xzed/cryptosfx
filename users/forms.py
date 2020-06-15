from django import forms
from django.forms import ModelForm, CharField, TextInput, PasswordInput, FileInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name',
                  'idcard', 'country', 'phone', 'currency', 'password1', 'password2')
        widgets = {'idcard': FileInput(attrs={'class': 'blackme'}), 'first_name': TextInput(attrs={'class': 'blackme', 'placeholder': 'Firstname'}), 'last_name': TextInput(
            attrs={'class': 'blackme', 'placeholder': 'Lastname'}), 'phone': TextInput(
            attrs={'class': 'blackme', 'placeholder': 'Phone Number'}), 'email': TextInput(
            attrs={'class': 'blackme', 'placeholder': 'Email'}),  'username': TextInput(
            attrs={'class': 'blackme', 'placeholder': 'Username'}), 'password1': PasswordInput(attrs={'id': 'blackme',
                                      'type': 'password',
                                      'required': 'true',}), }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name',
                  'idcard', 'country', 'phone', 'currency')
