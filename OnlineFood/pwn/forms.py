from django import forms
from pwn.models import StateModel,CityModel,CuisineModel
from django.forms import PasswordInput,DateInput,NumberInput,TimeInput

class Stateform(forms.ModelForm):
    class Meta:
        model=StateModel
        fields="__all__"
        labels={"name":"State Name","photo":"Photo"}

class Cityform(forms.ModelForm):
    class Meta:
        model=CityModel
        fields="__all__"
        labels={"name":"State Name","photo":"Photo"}

class Cuisineform(forms.ModelForm):
    class Meta:
        model=CuisineModel
        fields="__all__"
        labels={"name":"State Name","photo":"Photo"}
