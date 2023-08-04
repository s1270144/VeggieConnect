from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class PurchaseForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='購入数')

    def __init__(self, *args, **kwargs):
        max_quantity = kwargs.pop('max_quantity', None)
        super().__init__(*args, **kwargs)
        if max_quantity is not None:
            self.fields['quantity'].widget.attrs['max'] = max_quantity

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        max_quantity = self.fields['quantity'].widget.attrs.get('max')
        if max_quantity is not None and quantity > max_quantity:
            raise forms.ValidationError('在庫数を超える数量は選択できません。')
        return quantity
