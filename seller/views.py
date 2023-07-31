from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Seller
from accounts.models import UserManager
from accounts.forms import UserProfileForm
from django.views import View
from .forms import ItemForm

@login_required
def seller_home(request):
    user = request.user
    try:
        seller = Seller.objects.get(user=user)
        form = UserProfileForm(request.POST, request.FILES)
        return render(request, 'seller/home.html', {'seller': seller})
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
            return redirect('seller:home') # リダイレクト先は適宜変更してください

        return render(request, self.template_name, {'form': form})
