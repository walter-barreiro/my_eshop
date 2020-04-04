import datetime

from django.shortcuts import render, redirect

from search_product.models import Product
from shopping_cart.models import Order, OrderItem
from user_account.models import Customer


def payment(request):
    owner = Customer.objects.filter(user=request.user).first()
    order = Order.objects.filter(owner=owner).first()
    return render(request, 'payment/payment.html', {'order': order})


def pay(request):
    owner = Customer.objects.filter(user=request.user).first()
    order = Order.objects.filter(owner=owner).first()
    for item in order.items.all():  # Para cada item en order
        if not item.pay:  # Si pay=False (La orden no se ha pagado)
            product = Product.objects.filter(pk=item.product.pk).first()  # Busco el producto de ese item
            product.in_cart = product.in_cart - int(item.quantity)  # Le resto al carrito del producto la cantidad
            product.stock = product.stock - int(item.quantity)  # Actualizo el stock del producto
            product.sales = product.sales + item.quantity
            product.save()
            item.name = item.product.name
            item.buy_price = item.product.price
            item.pay = True
            item.pay_date = datetime.datetime.now()
            item.save()
    return render(request, 'payment/payment.html', {})
    # return redirect("home")
