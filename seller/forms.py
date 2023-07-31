from django import forms
from .models import Vegetable
from django.utils.translation import gettext_lazy as _

class ItemForm(forms.ModelForm):
    class Meta:
        model = Vegetable
        fields = ['item_name', 'item_type', 'content_quantity', 'content_price', 'total_quantity']

        # フィールドのラベルを日本語に設定
        labels = {
            'item_name': _('品目名'),
            'item_type': _('品種名'),
            'content_quantity': _('内容量（個数）'),
            'content_price': _('価格/袋'),
            'total_quantity': _('出品総数'),
        }
