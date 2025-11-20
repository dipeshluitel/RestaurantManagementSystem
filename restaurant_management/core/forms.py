from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_type','table_number','notes']

        widgets = {
            'customer_type': forms.Select(attrs={'class':'form-control'}),
            'table_number': forms.Select(attrs={'class':'form-control'}),
            'notes': forms.Textarea(attrs={'class':'form-control'}),
        }