from django.urls import path
from . import views

app_name = 'shopping_history'

urlpatterns = [
    path('shopping_history/', views.shopping_history, name="shopping_history"),
]
