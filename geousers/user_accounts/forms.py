from django import forms
from .models import Account
from leaflet.forms.widgets import LeafletWidget

class AccountForm(forms.ModelForm):
    """Form for creating new user accounts."""
    
    class Meta:
        model = Account
        fields = ['home_address', 'phone_number', 'location']
        widgets = {
            'location': LeafletWidget(),
        }