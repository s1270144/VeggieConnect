from django.urls import path

from . import views

app_name = "seller"

urlpatterns = [
    path("", views.seller_home, name="home"),
]
