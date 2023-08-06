from django.db import models
from accounts.models import User

# 出品者
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller')
    address = models.CharField(max_length=200)

    def __str__(self):
        return str(self.user_id)


# 商品情報
class Product(models.Model):
    MAIN_GENRE_CHOICES = (
        ('Grains', '穀物類'),
        ('Vegetables', '野菜類'),
        ('Fruits', '果物類'),
        ('Others', 'その他'),
    )
    SUB_GENRE_CHOICES = (
        ('---', '---'),
        ('LeafStem', '葉茎菜類'),
        ('Root', '根菜類'),
        ('Fruit', '果菜類'),
        ('Others', 'その他'),
    )

    item_name = models.CharField(max_length=100, primary_key=True)
    main_genre_name = models.CharField(max_length=100, choices=MAIN_GENRE_CHOICES)
    sub_genre_name = models.CharField(max_length=100, choices=SUB_GENRE_CHOICES, blank=True, default='---')

    class Meta:
        permissions = [
            ('can_edit_product', 'Can edit product'),  # 編集権限
        ]

    def __str__(self):
        return f"{self.item_name}"


# 出品商品
class Vegetable(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='vegetable')      # 出品者
    item_name = models.ForeignKey(Product, on_delete=models.CASCADE, default=None, null=True)   # 商品
    item_type = models.CharField(max_length=100, default='---')                                 # 品種名
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0)                    # 単価
    content_quantity = models.PositiveIntegerField(default=1)                                   # まとまりの内容個数
    content_price = models.DecimalField(max_digits=100, decimal_places=2, default=0)            # まとまりの価格
    total_quantity = models.PositiveIntegerField(default=0)                                     # まとまりの総数

    def __str__(self):
        return str(self.seller.id)
