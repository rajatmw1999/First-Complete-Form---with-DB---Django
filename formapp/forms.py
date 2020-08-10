from django import forms
from django.core import validators
from formapp.models import FormData


class NewUser(forms.ModelForm):
    #inline meta class that stores data to db
    class Meta:
        model = FormData
        fields = '__all__'
