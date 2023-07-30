from django.db import models

class Seller(models.Model):
    # 出品者の情報に関連するフィールドを定義
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    # 他に出品者の情報を表すフィールドを追加

    def __str__(self):
        return self.name

class Vegetable(models.Model):
    # 野菜の情報に関連するフィールドを定義
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    # 他に野菜の情報を表すフィールドを追加

    def __str__(self):
        return self.name
