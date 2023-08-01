from django.urls import path

from .views import SellerHomeView, CreateItemView

app_name = "seller"

urlpatterns = [
    path("home/", SellerHomeView.as_view(), name="home"),
    path('create/', CreateItemView.as_view(), name='create_item'),
]
