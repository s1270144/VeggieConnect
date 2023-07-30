from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as BaseLoginView,  LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginFrom


class IndexView(TemplateView):
    template_name = "accounts/index.html"


class SignupView(CreateView):
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:index")

    def signup(self, request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_seller = form.cleaned_data['is_seller']  # フォームの値をis_sellerに代入
                user.save()
                return redirect('buyer:home')  # 登録後にリダイレクトするページを指定
        else:
            form = SignUpForm()
        return render(request, 'accounts/login', {'form': form})


class LoginView(BaseLoginView):
    form_class = LoginFrom
    template_name = "accounts/login.html"
    success_url = reverse_lazy('buyer:home')


class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("accounts:index")
