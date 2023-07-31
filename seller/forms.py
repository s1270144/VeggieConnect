from django import forms
from .models import Vegetable

class ItemForm(forms.ModelForm):
    class Meta:
        model = Vegetable
        fields = ['item_name', 'item_type', 'stock_quantity', 'price']
