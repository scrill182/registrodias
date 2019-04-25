
from django import forms

from .models import Registro

class PostForm(forms.ModelForm):

    class Meta:
        model = Registro
        fields = ('nombre', 'diasFestivos ',)