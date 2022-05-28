from dataclasses import field
from django import forms

from .models import threeDmodels

class MyModelForm(forms.ModelForm):
    class Meta:
        model = threeDmodels
        fields = ('name', 'modelfile')