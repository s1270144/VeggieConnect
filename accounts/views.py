from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as BaseLoginView,  LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginFrom
from buyer.models import Buyer
from seller.models import Seller


class IndexView(TemplateView):
    template_name = "accounts/index.html"


class SignupView(CreateView):
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:index")

    def form_valid(self, form):
        response = super().form_valid(form)

        is_seller = form.cleaned_data['is_seller']

        # Buyerモデルのインスタンスを作成して保存する
        buyer = Buyer.objects.create(user=self.object, address="some_address", favorite="some_favorite")
        if is_seller:
            # ユーザーが出品者の場合、Sellerモデルのインスタンスを作成して保存する
            seller = Seller.objects.create(user=self.object, address="some_address")

        return response


class LoginView(BaseLoginView):
    form_class = LoginFrom
    template_name = "accounts/login.html"
    success_url = reverse_lazy('buyer:home')


class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("accounts:index")
