from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'main_genre_name', 'sub_genre_name')
    search_fields = ('item_name', 'main_genre_name', 'sub_genre_name')

admin.site.register(Product, ProductAdmin)
