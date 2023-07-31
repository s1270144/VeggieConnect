from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import User


class SignUpForm(UserCreationForm):
    is_seller = forms.BooleanField(required=False, label=_('出品します。'), widget=forms.CheckboxInput(attrs={'class': 'checkbox-class'}))

    class Meta:
        model = User
        fields = ('account_id', 'email', 'last_name', 'first_name', 'birth_date', 'is_seller')

        # フィールドのラベルを日本語に設定
        labels = {
            'account_id': _('アカウントID'),
            'email': _('メールアドレス'),
            'last_name': _('姓'),
            'first_name': _('名'),
            'birth_date': _('生年月日'),
            'is_seller': _('出品します。')
        }


# ログインフォームを追加
class LoginFrom(AuthenticationForm):
    class Meta:
        model = User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'address', 'profile_picture')
