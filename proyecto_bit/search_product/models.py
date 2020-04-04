from django.db import models

from category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=50)
    stock = models.IntegerField(default=0)           # Stock maximo
    in_cart = models.IntegerField(default=0)         # Cantidad de productos que los clientes tienen en sus carritos
    sales = models.IntegerField(default=0)           # Ventas realizadas hasta el momento de este producto
    quantity_1 = models.IntegerField(default=0)      # Primer cantidad a la que se tiene que llegar para que el
    quantity_2 = models.IntegerField(default=0)      # producto valga price_1
    quantity_3 = models.IntegerField(default=0)
    price_1 = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price_2 = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price_3 = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    discount = models.BooleanField(default=False)
    new_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    
    def __str__(self):
        return self.name
