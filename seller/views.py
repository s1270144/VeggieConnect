from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Seller, Vegetable
from accounts.models import UserManager
from accounts.forms import UserProfileForm
from django.views.generic import DetailView
from django.views import View
from .forms import ItemForm

from django.contrib.auth.mixins import LoginRequiredMixin


class SellerHomeView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'  # ログインしていない場合のリダイレクト先URL

    def get(self, request):
        user = request.user.id
        try:
            seller = Seller.objects.get(user_id=user)
            vegetables = Vegetable.objects.filter(seller_id=seller.id)
            form = UserProfileForm()
            return render(request, 'seller/home.html', {'vegetables': vegetables, 'form': form})
        except Seller.DoesNotExist:
            # ユーザが出品者でない場合の処理
            return render(request, 'seller/seller_not_found.html')


class CreateItemView(View):
    template_name = 'seller/create_item.html'

    def get(self, request):
        form = ItemForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            # ログインしているユーザーを出品者と紐付ける
            if request.user.is_authenticated:
                item.seller = request.user.seller
            item.save()
            return redirect('seller:home')

        return render(request, self.template_name, {'form': form})


class ProductDetailView(DetailView):
    model = Vegetable
    template_name = 'seller/product_detail.html'
    context_object_name = 'vegetable'
    pk_url_kwarg = 'vegetable_id'
