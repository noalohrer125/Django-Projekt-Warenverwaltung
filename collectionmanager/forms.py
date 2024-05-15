from unicodedata import category
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
        fields = [
            'username',
            'password1',
            'password2',
            'email',
            ]

from django import forms
from .models import Regale, Waren, Kategorie

class WareForm(forms.ModelForm):

    class Meta:
        model = Waren
        fields = [
            'producer',
            'name',
            'description',
            'price',
            'length',
            'width',
            'height',
            'category',
            'shelf',
            'story',
            'owner',
            'image',
            ]

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Kategorie
        fields = [
            'name',
            'description',
            ]
