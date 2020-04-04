from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'payment'

urlpatterns = [
    path('payment/', views.payment, name="payment"),
    path('pay/', views.pay, name="pay"),
]