from django import forms
from .models import signp_model


class Signup_form(forms.ModelForm):
    class Meta:
        model = signp_model
        fields = '__all__'