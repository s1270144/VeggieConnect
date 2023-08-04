from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Buyer
from seller.models import Vegetable
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PurchaseForm


User = get_user_model()


class BuyerHomeView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'  # ログインしていない場合のリダイレクト先URL
    def get(self, request):
        return render(request, 'buyer/home.html')


class VegetableListView(View):
    def get(self, request):
        vegetables = Vegetable.objects.all()
        return render(request, 'buyer/vegetable_list.html', {'vegetables': vegetables})


class ProductDetailView(DetailView):
    model = Vegetable
    template_name = 'buyer/product_detail.html'

    def get(self, request, vegetable_id):
        vegetable = get_object_or_404(Vegetable, pk=vegetable_id)
        form = PurchaseForm(initial={'max_quantity': vegetable.total_quantity})
        return render(request, self.template_name, {'vegetable': vegetable, 'form': form})

    def post(self, request, vegetable_id):
        vegetable = get_object_or_404(Vegetable, pk=vegetable_id)

        form = PurchaseForm(request.POST, initial={'max_quantity': vegetable.total_quantity})
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            print(quantity)
            # 在庫数と購入数を比較して、在庫を超えないようにする
            if quantity <= vegetable.total_quantity:
                # 在庫数を更新
                vegetable.total_quantity -= quantity
                print(vegetable.total_quantity)
                vegetable.save()
                return redirect('buyer:purchase_complete')

        return render(request, self.template_name, {'vegetable': vegetable, 'form': form})


class PurchaseCompleteView(View):
    def get(self, request):
        return render(request, 'buyer/purchase_complete.html')
