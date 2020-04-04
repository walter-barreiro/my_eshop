from django.urls import path
from . import views

app_name = 'search_product'

urlpatterns = [
    path('search_product/', views.search_product, name="search_product"),
    path('add_to_cart/', views.add_to_cart, name="add_to_cart"),
]
