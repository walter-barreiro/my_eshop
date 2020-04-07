from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True )
    name = models.CharField(max_length=20, null=True)
    lastname = models.CharField(max_length=20, null=True)
    # gender = models.Choices()
    birthday = models.DateTimeField(null=True, default=datetime.now)
    phone = models.CharField(max_length=20, null=True)
    address = models.TextField(null=True)
    country = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    money = models.DecimalField(null=True, max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return 'Username: ' + self.user.email
