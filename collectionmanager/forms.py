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
        fields = UserCreationForm.Meta.fields + ('email',)

from django import forms
from .models import Regale, Waren, Kategorie

class WareForm(forms.ModelForm):
    Kategorie = forms.ModelChoiceField(queryset=Kategorie.objects.all(), required=False)
    Regal = forms.ModelChoiceField(queryset=Regale.objects.all(), required=False)

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
            'Geschichte',
            'Eigentümer',
            'bild',
            ]

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Kategorie
        fields = [
            'name',
            'Beschreibung',
            ]
