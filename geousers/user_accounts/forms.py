from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['home_address', 'phone_number', 'location']
        widgets = {
            'location': forms.HiddenInput()
        }