from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .models import Buyer


User = get_user_model()


@login_required
def buyer_home(request):
    return render(request, 'buyer/home.html')

def register_user(request):
    if request.method == 'POST':
        # ユーザー情報を取得してUserモデルに保存
        account_id = request.POST['account_id']
        email = request.POST['email']
        last_name = request.POST['last_name']
        birth_date = request.POST['birth_date']
        password = request.POST['password']

        user = User.objects.create_user(account_id=account_id, email=email, last_name=last_name, birth_date=birth_date, password=password)

        # Buyerモデルに関連するインスタンスを作成
        address = request.POST['address']
        favorite = request.POST['favorite']
        buyer = Buyer(user=user, address=address, favorite=favorite)
        buyer.save()

        return redirect('buyer:home')
    else:
        return render(request, 'accounts/register.html')
