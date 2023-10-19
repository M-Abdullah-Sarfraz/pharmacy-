from django import forms
from .models import contact_model

class getintouch_form(forms.ModelForm):
    class Meta:
        model = contact_model
        fields = '__all__'