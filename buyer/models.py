from django.db import models
from accounts.models import User

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='buyer')
    address = models.CharField(max_length=200)
    favorite = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user_id)

class Transaction(models.Model):
    purchase_id = models.CharField(max_length=100, unique=True)
    # user_id = models.CharField(max_length=100)
    # item_id = models.CharField(max_length=100)
    # purchase_date = models.DateTimeField()
    # purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    # quantity = models.IntegerField()
    purchase_status = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    shipping_info = models.TextField()
    billing_info = models.TextField()
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.purchase_id)
