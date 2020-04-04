from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'discounts'

urlpatterns = [
    path('discounts/', views.discounts, name="discounts"),
    path('apply_discounts/', views.apply_discounts, name="apply_discounts"),
]