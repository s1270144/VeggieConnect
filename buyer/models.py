from django.db import models
from accounts.models import User

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='buyer')
    address = models.CharField(max_length=200)
    favorite = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email
