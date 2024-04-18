from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta:
        model=User
        fields = UserCreationForm.Meta.fields + ('email',)

from django import forms
from .models import Waren

class WareForm(forms.ModelForm):
    class Meta:
        model = Waren
        fields = [
            'Hersteller',
            'name',
            'description',
            'price',
            'length',
            'width',
            'height',
            'Kategorie',
            'Regal',
            'Kaufdatum',
            'Geschichte',
            'Eigentümer',
            ]
