from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms
from.models import User


class UserRegistration(UserCreationForm):
    username = forms.CharField(label='Username', max_length=24, min_length=3,
                               widget=forms.TextInput(attrs={"class": 'login-input'}))

    email = forms.EmailField(label='Email', max_length=64,
                             widget=forms.EmailInput(attrs={"class": 'email-input'}))

    password1 = forms.CharField(label='Password', max_length=24, min_length=4,
                                widget=forms.PasswordInput(attrs={'class': 'psswrd-input'}))

    password2 = forms.CharField(label='Password confirmation', max_length=24, min_length=4,
                                widget=forms.PasswordInput(attrs={'class': 'psswrd-input'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        users_with_same_username = User.objects.filter(username=username)
        if users_with_same_username:
            raise ValidationError("Username must be unique, sorry.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        users_with_same_email = User.objects.filter(email=email)
        if users_with_same_email:
            raise ValidationError("Email must be unique, sorry.")
        return email
