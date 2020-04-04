from django import forms
from .models import Customer


class UserAccount(forms.Form):
    name = forms.CharField(label='Nombre', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=20, label='Celular', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Direccion', widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.CharField(label='Pais', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(label='Ciudad', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))




#     class Meta:
#         model = Customer
#
#         fields = [
#             'name',
#             'phone',
#             'address',
#             'country',
#             'city',
#         ]
#         labels = {
#             'name': 'Name',
#             'phone': 'Phone',
#             'address': 'Address',
#             'country': 'Country',
#             'city': 'City',
#         }
#         # widget = {
#         #     'name': forms.TextInput(attrs={'class': 'form-control'}),
#         #     'phone': 'Phone',
#         #     'address': 'Address',
#         #     'country': 'Country',
#         #     'city': 'City',
#         # }


