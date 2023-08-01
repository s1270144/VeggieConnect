from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views import View
from .models import Buyer
from seller.models import Vegetable
from django.contrib.auth.mixins import LoginRequiredMixin


User = get_user_model()


class BuyerHomeView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'  # ログインしていない場合のリダイレクト先URL

    def get(self, request):
        return render(request, 'buyer/home.html')


class VegetableListView(View):
    def get(self, request):
        vegetables = Vegetable.objects.all()
        return render(request, 'buyer/vegetable_list.html', {'vegetables': vegetables})
