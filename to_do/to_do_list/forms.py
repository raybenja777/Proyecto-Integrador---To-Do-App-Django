from django import forms
from .models import CustomUser

class RegistroForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('Usuario_Email', 'Constraseña')
