from django import forms
from .models import Partner

class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner  # Connect this form to the Partner model
        fields = ['name', 'contact_info'] 