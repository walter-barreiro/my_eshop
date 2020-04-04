from django.urls import path
from . import views

app_name = 'shopping_cart'

urlpatterns = [
    path('shopping_cart/', views.shopping_cart, name="shopping_cart"),
    path('delete_from_cart/', views.delete_from_cart, name="delete_item"),
]
