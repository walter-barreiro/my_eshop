from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from shopping_cart.models import OrderItem, Order
from user_account.models import Customer
from .models import Product
from django.db.models import Q


def search_product(request):
    query = request.POST.get('query', '')
    allProducts = Product.objects.filter(
        Q(name__icontains=query) | Q(price__icontains=query) | Q(description__icontains=query)
    )
    if request.user.is_authenticated: # Para eliminar un error que saltaba
        owner = Customer.objects.filter(user=request.user).first()
        order = Order.objects.filter(owner=owner).first()
        order_items = order.items.all()
        products_id = set()  # Conjunto creado para guardar todos los id de productos que estan en el carrito del client
        for item in order_items:  # se guardan todos los id del productos que el cliente tiene en el carrito
            if not item.pay:
                products_id.add(item.product.pk)
        context = {'allProducts': allProducts, 'products_id': products_id}
    else:
        context = {'allProducts': allProducts}
    return render(request, 'search_product/search_product.html', context)


def add_to_cart(request):
    product_id = request.POST.get('product_id', '')
    quantity = request.POST.get('quantity', '')
    product = Product.objects.filter(pk=product_id).first()
    if int(product.stock) < int(quantity):
        messages.error(request, "No hay suficiente stock ")
    else:
        # Actualizo el carrito
        product.in_cart = product.in_cart + int(quantity)
        product.save()
        # ------------------------------------------------
        owner = Customer.objects.filter(user=request.user).first()
        order_item = OrderItem(product=product, quantity=quantity)
        order_item.save()
        order = Order.objects.filter(owner=owner).first()
        order.items.add(order_item)
    return redirect(reverse('search_product:search_product'))
