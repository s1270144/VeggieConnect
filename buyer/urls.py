from django.urls import path
from .views import (BuyerHomeView, VegetableListView, ProductDetailView,
                    PurchaseCompleteView, TransactionListView, TransactionDetailView,
                    GenreFirstView, GenreVegetableView, GenreDetailView, ErrorBCView, NothingProductView)

app_name = "buyer"

urlpatterns = [
    path("home/", BuyerHomeView.as_view(), name="home"),
    path('vegetable_list/', VegetableListView.as_view(), name='vegetable_list'),
    path('product/<int:vegetable_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('genre/', GenreFirstView.as_view(), name='genre'),
    path('genre/genre_vegetable/', GenreVegetableView.as_view(), name='genre_vegetable'),
    path('genre/<str:genre_name>/', GenreDetailView.as_view(), name='genre_name'),
    path('purchase_complete/', PurchaseCompleteView.as_view(), name='purchase_complete'),
    path('transaction_list/', TransactionListView.as_view(), name='transaction_list'),
    path('transaction_list/<int:vegetable_id>/<uuid:transaction_id>/', TransactionDetailView.as_view(), name='transaction_detail'),
    path('blockchain_error/', ErrorBCView.as_view(), name='blockchain_error'),
    path('nothing_purchased_product/', NothingProductView.as_view(), name='nothing_purchased_product'),
]
