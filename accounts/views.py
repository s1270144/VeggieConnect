from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as BaseLoginView,  LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginFrom, UserProfileForm
from buyer.models import Buyer
from seller.models import Seller
from django.views import View
from .forms import UserProfileForm


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
        buyer = Buyer.objects.create(user=self.object, address="---", favorite="---")
        if is_seller:
            # ユーザーが出品者の場合、Sellerモデルのインスタンスを作成して保存する
            seller = Seller.objects.create(user=self.object, address="---")

        return response


class LoginView(BaseLoginView):
    form_class = LoginFrom
    template_name = "accounts/login.html"
    success_url = reverse_lazy('buyer:home')


class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("accounts:index")


class EditProfileView(View):
    template_name = 'accounts/edit_profile.html'

    def get(self, request):
        form = UserProfileForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:view_profile')
        return render(request, self.template_name, {'form': form})
