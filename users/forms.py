from django import forms
from django.forms import ModelForm, CharField, TextInput, PasswordInput, FileInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None) 

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
                                                                                                      'required': 'true', }), }
    def send_email(self):
        subject, from_email, to = 'New User Registration', 'helpbox@coinwintrade.com', self.cleaned_data.get("email")
        c = {'username':self.cleaned_data.get("first_name") + ' ' + self.cleaned_data.get("last_name"),'email':self.cleaned_data.get('email'),'password':self.cleaned_data.get('password1') }  
        html_content = render_to_string('email.html', c) # render with dynamic value
        text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.
        
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        pass    


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name',
                  'idcard', 'country', 'phone', 'currency','balance')
