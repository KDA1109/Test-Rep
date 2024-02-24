from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('clients/', views.clients, name='clients'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),
    path('client_orders/<int:client_id>/', views.client_orders, name='client_orders'),
    path('product_up/<int:product_id>', views.update_product, name='update_product'),
]