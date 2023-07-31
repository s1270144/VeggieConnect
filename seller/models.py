from django.db import models
from accounts.models import User

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller')
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user.email

class Vegetable(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)                        # 出品者
    item_name = models.CharField(max_length=100)                                        # 品目名
    item_type = models.CharField(max_length=100)                                        # 品種名
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0)            # 単価
    content_quantity = models.PositiveIntegerField(default=1)                           # まとまりの内容個数
    content_price = models.DecimalField(max_digits=100, decimal_places=2, default=0)    # まとまりの価格
    total_quantity = models.PositiveIntegerField(default=0)                             # まとまりの総数

    def __str__(self):
        return self.name
