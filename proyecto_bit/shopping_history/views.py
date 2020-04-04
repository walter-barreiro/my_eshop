from django.shortcuts import render

from shopping_cart.models import Order
from user_account.models import Customer


def shopping_history(request):
    owner = Customer.objects.filter(user=request.user).first()
    order = Order.objects.filter(owner=owner).first()
    return render(request, 'shopping_history/shopping_history.html', {'order': order})

