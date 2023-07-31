from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Seller
from accounts.models import UserManager
from accounts.forms import UserProfileForm

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
