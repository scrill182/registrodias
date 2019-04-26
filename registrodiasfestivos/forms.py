
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Registro


class PostForm(forms.ModelForm):

    class Meta:
        model = Registro
        fields = ('nombre','no_cobro','diasFestivos','horario')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))
