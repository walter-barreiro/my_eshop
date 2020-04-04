from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import OrderItem, Order
from user_account.models import Customer
from search_product.models import Product
from django.contrib import messages


@login_required(login_url='login')  # Para que solo pueda acceder si esta logueado
def shopping_cart(request):
    owner = Customer.objects.filter(user=request.user).first()
    order = Order.objects.filter(owner=owner).first()
    return render(request, 'shopping_cart/shopping_cart.html', {'order': order})


@login_required(login_url='login')  # Para que solo pueda acceder si esta logueado
def delete_from_cart(request):
    delete_item = request.POST.get('delete_item', '')
    item_to_delete = OrderItem.objects.filter(pk=delete_item)
    product_id = item_to_delete.first().product.pk  # El id del producto que pertenece al OrderItem actual
    quantity = item_to_delete.first().quantity  # La cantidad de productos del OrderItem actual
    if item_to_delete.exists():
        product = Product.objects.filter(pk=product_id).first()
        product.in_cart = product.in_cart - int(quantity)
        product.save()
        item_to_delete[0].delete()
    return redirect(reverse('shopping_cart:shopping_cart'))




