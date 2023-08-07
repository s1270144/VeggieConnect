from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Buyer, Transaction
from seller.models import Vegetable, Product
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PurchaseForm
import uuid
from .blockchain.func.get_numTransaction import get_numtx
from .blockchain.func.get_detail import get_detail
from .blockchain.func.get_transactionInfo import get_tx
from .blockchain.func.set_transaction import set_info
import datetime
from django.db.models import Q


User = get_user_model()


class BuyerHomeView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'  # ログインしていない場合のリダイレクト先URL
    template_name = 'buyer/home.html'
    def get(self, request):
        return render(request, self.template_name)


class VegetableListView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    template_name = 'buyer/vegetable_list.html'
    def get(self, request):
        vegetables = Vegetable.objects.all()
        # print(vegetables)
        return render(request, self.template_name, {'vegetables': vegetables})


class ProductDetailView(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login/'
    model = Vegetable
    template_name = 'buyer/product_detail.html'

    def get(self, request, vegetable_id):
        vegetable = get_object_or_404(Vegetable, pk=vegetable_id)
        form = PurchaseForm(initial={'max_quantity': vegetable.total_quantity})
        form.fields['quantity'].widget.attrs['max'] = vegetable.total_quantity
        return render(request, self.template_name, {'vegetable': vegetable, 'form': form})

    def post(self, request, vegetable_id):
        vegetable = get_object_or_404(Vegetable, pk=vegetable_id)

        form = PurchaseForm(request.POST, initial={'max_quantity': vegetable.total_quantity})
        if form.is_valid():
            purchase_id = str(uuid.uuid4())
            user = request.user.id
            item_id = vegetable_id
            quantity = form.cleaned_data['quantity']
            purchase_price = int(vegetable.content_price * quantity)
            purchase_status = '---'
            payment_method = '---'
            shipping_info = '---'
            billing_info = '---'
            additional_info = '---'
            transaction = Transaction.objects.create(
                purchase_id=purchase_id,
                purchase_status=purchase_status,
                payment_method=payment_method,
                shipping_info=shipping_info,
                billing_info=billing_info,
                additional_info=additional_info
            )
            transaction.save()
            try:
                set_info(purchase_id, str(user), str(item_id), str(purchase_price), str(quantity))
            except:
                pass
            # 在庫数と購入数を比較して、在庫を超えないようにする
            if quantity <= vegetable.total_quantity:
                # 在庫数を更新
                vegetable.total_quantity -= quantity
                vegetable.save()
                return redirect('buyer:purchase_complete')

        return render(request, self.template_name, {'vegetable': vegetable, 'form': form})


class PurchaseCompleteView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    template_name = 'buyer/purchase_complete.html'
    def get(self, request):
        return render(request, self.template_name)


class TransactionListView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    template_name = 'buyer/transaction_list.html'

    def get(self, request):
        user = request.user.id
        try:
            tx_list = get_tx(str(user))
            l = []
            try:
                print(tx_list['output'])
                for vege in tx_list['output']:
                    l.append(vege['item_id'])
                vegetables = Vegetable.objects.filter(id__in=l)
                vegetable_and_transaction = zip(vegetables, tx_list['output'])
                return render(request, self.template_name, {'vegetable_and_transaction': vegetable_and_transaction})
            except Exception as e:
                print ('=== エラー内容 ===')
                print ('type:' + str(type(e)))
                print ('args:' + str(e.args))
                print ('message:' + e.message)
                print ('e自身:' + str(e))
        except Exception as e:
            print ('=== エラー内容 ===')
            print ('type:' + str(type(e)))
            print ('args:' + str(e.args))
            print ('message:' + e.message)
            print ('e自身:' + str(e))
            return render(request, 'buyer/home.html')


class TransactionDetailView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    template_name = 'buyer/transaction_detail.html'

    def get(self, request, vegetable_id, transaction_id):
        vegetable = get_object_or_404(Vegetable, pk=vegetable_id)
        tx_detail = get_detail(transaction_id)
        timestamp = int(tx_detail['output']['purchase_date'][:10])
        dt = datetime.datetime.fromtimestamp(timestamp)
        tx_detail['output']['purchase_date'] = str(dt)
        return render(request, self.template_name, {'vegetable': vegetable, 'tx_detail': tx_detail['output']})


class GenreFirstView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    template_name = 'buyer/genre.html'
    def get(self, request):
        products = Product.objects.all()
        return render(request, self.template_name, {'products': products})


class GenreVegetableView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    template_name = 'buyer/genre_vegetable.html'
    def get(self, request):
        products = Product.objects.all()
        return render(request, self.template_name, {'products': products})


class GenreDetailView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    template_name = 'buyer/vegetable_list.html'
    def get(self, request, genre_name):
        if '-' in genre_name:
            left_side, right_side = genre_name.split("-")
            grains_items = Product.objects.filter(Q(main_genre_name=left_side) & Q(sub_genre_name=right_side)).values_list("item_name", flat=True)
        else:
            grains_items = Product.objects.filter(main_genre_name=genre_name).values_list("item_name", flat=True)
        vegetables = Vegetable.objects.filter(item_name__in=grains_items)
        return render(request, self.template_name, {'vegetables': vegetables})
