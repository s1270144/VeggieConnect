from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/accounts/')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('buyer/', include('buyer.urls')),
    path('seller/', include('seller.urls')),
]
