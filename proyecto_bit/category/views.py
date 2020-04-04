from django.shortcuts import render

from search_product.models import Product


def search_category(request):
    product = Product.objects.all()
    query = ""  # Filtro por defecto
    if request.POST.get('query'):
        query = request.POST.get('query')
        product = Product.objects.filter(category=query)
    return render(request, "category/search_category.html", {'products': product})