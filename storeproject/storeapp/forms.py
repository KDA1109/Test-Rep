from django import forms
from .models import Client, Product, Order



class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone_number',  'address']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'price', 'product_amount', 'foto']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['id', 'client_id', 'product_id', 'total_price', 'status']