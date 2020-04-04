import datetime

from django.db import models
from search_product.models import Product
from user_account.models import Customer


class OrderItem(models.Model):
    name = models.CharField(max_length=30, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True, default=1)
    # Guarda el precio al que se compro el producto
    buy_price = models.DecimalField(max_digits=8, decimal_places=2,  null=True)
    # Indica si ya se pago el item
    pay = models.BooleanField(default=False, null=True)
    # Indica si ya se le aplico el descuento
    discounted = models.BooleanField(default=False, null=True)
    # Indica el precio del producto luego del descuento
    new_price = models.DecimalField(max_digits=8, decimal_places=2,  null=True)
    # Guarda la fecha y hora en la que se realizo el pago
    pay_date = models.DateTimeField(default=datetime.datetime.now(), null=True)

    def __str__(self):
        return self.product.name

    def sub_total(self):        # Calcula el subtotal antes de la compra
        return self.quantity * self.product.price

    def sub_total_history(self): # Calcula el subtoral luego de la compra
        return self.quantity * self.buy_price

    def new_sub_total(self):    # Calcula el subtotal luego de aplicar el descuento
        return self.quantity * self.new_price


class Order(models.Model):
    owner = models.OneToOneField(Customer, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(OrderItem)

    def total(self):    # Calcula el total a pagar antes de realizar la compra
        total = 0
        for item in self.items.all():
            if not item.pay:
                total = total + item.sub_total()
        return total
