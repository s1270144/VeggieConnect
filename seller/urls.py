from django.urls import path

from .views import SellerHomeView, CreateItemView, ProductDetailView, EditItemView

app_name = "seller"

urlpatterns = [
    path("home/", SellerHomeView.as_view(), name="home"),
    path('create/', CreateItemView.as_view(), name='create_item'),
    path('product/<int:vegetable_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('edit/<int:vegetable_id>', EditItemView.as_view(), name='edit_item')
]
