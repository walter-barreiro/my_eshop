from django.urls import path
from . import views

app_name = 'category'

urlpatterns = [
    path('search_category/', views.search_category, name="search_category"),
]
