from django import forms
from .models import veriler

class VeriForm(forms.ModelForm):
    class Meta:
        model = veriler
        fields = ['kullaniciadi', 'sifre']