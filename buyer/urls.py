from django.urls import path
from .views import BuyerHomeView, VegetableListView, ProductDetailView, PurchaseCompleteView

app_name = "buyer"

urlpatterns = [
    path("home/", BuyerHomeView.as_view(), name="home"),
    path('vegetable_list/', VegetableListView.as_view(), name='vegetable_list'),
    path('product/<int:vegetable_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('purchase_complete/', PurchaseCompleteView.as_view(), name='purchase_complete'),

]
