from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class PurchaseForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='購入数')

    def __init__(self, *args, **kwargs):
        max_quantity = kwargs.pop('max_quantity', None)
        super(PurchaseForm, self).__init__(*args, **kwargs)
        if max_quantity is not None:
            self.fields['quantity'].validators.append(
                MaxValueValidator(max_value=max_quantity, message=f"在庫数は{max_quantity}以下にしてください。")
            )
