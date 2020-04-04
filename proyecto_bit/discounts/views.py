import datetime

from django.shortcuts import render, redirect

from discounts.models import DateDiscount
from search_product.models import Product
from shopping_cart.models import Order
from user_account.models import Customer


def discounts(request):
    owner = Customer.objects.filter(user=request.user).first()
    order = Order.objects.filter(owner=owner).first()
    return render(request, 'discounts/discounts.html', {'order': order, 'owner': owner})


def apply_discounts(request):
    # Recorro los productos para ver si se aplican descuentos
    for product in Product.objects.all():  # Recorro todos los productos
        if product.sales >= product.quantity_3:  # Me fijo si se superaron las cantidades minimas para aplicar descuento
            product.new_price = product.price_3  # Le asigno a new_price el precio correspondiente al desceutno
            product.discount = True  # Indico que este producto si tiene descuento
            product.sales = 0       # Reseteo las ventas a cero
            product.save()
        elif product.quantity_3 >= product.sales >= product.quantity_2:
            product.sales = 0
            product.new_price = product.price_2
            product.discount = True
            product.save()
        elif product.quantity_2 >= product.sales >= product.quantity_1:
            product.sales = 0
            product.new_price = product.price_1
            product.discount = True
            product.save()
        else:
            product.sales = 0
            product.save()
    # Aplico los descuentos a cada cliente
    for customer in Customer.objects.all():  # Recorro cada cliente
        order = Order.objects.filter(owner=customer).first()  # Extraigo la orden de ese cliente
        for item in order.items.all():  # Recorro cada item de esa orden
            # Extraigo la ultima vez que se hizo descuento
            last_discount_date = DateDiscount.objects.filter(pk=1).first()
            # Me fijo si:
            # el producto de esa orden tiene descuento
            # si aun no se le ha aplicado el descuento al producto
            # Si la compra se realizo luego de aplicado el utlimo descuento
            if item.product.discount and (not item.discounted) and item.pay_date > last_discount_date.date:
                item.new_price = item.product.new_price  # Le asigno el precio nuevo
                customer.money = customer.money + (item.sub_total() - item.new_sub_total())  # Calculo la ganancia
                item.discounted = True  # Indico que al producto ya se le aplico el descuento
                item.save()
                customer.save()

    # Luego de aplicar los descuentos, desactivo los descuentos
    for product in Product.objects.all():
        product.discount = False
        product.save()

    # Guardo la fecha en la que se hizo este descuento
    DateDiscount.objects.filter(pk=1).update(date=datetime.datetime.now())

    return render(request, "main/index.html", {})
