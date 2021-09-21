from django import forms
from django.forms import fields
from .models import predio

class PredioForm(forms.ModelForm):
    class Meta:
        model = predio
        fields = ['cedula_catastral','direccion','tipo','identificacion']
        