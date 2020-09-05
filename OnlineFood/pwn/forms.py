from django import forms
from pwn.models import StateModel
from django.forms import PasswordInput,DateInput,NumberInput,TimeInput

class Stateform(forms.ModelForm):
    class Meta:
        model=StateModel
        fields="__all__"
        labels={"name":"State Name","photo":"Photo"}