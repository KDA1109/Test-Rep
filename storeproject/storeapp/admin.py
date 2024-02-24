from django.contrib import admin
from .models import Client, Product, Order
from django.db.models import F

class StoreClient(admin.ModelAdmin):

    #@admin.action()

    list_display = ['name', 'email', 'phone_number', 'address']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Имя клиента (NAME)'
    ordering = ['name']
    list_filter = ['name']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Номер телефона и адрес',
                'fields': ['phone_number', 'address'],
            },
        ),
        (
            'Электронная почта',
            {
                'description': 'Электронная почта',
                'fields': ['email'],
            }
        ),
    ]


class StoreProduct(admin.ModelAdmin):

    @admin.action(description='Увеличить цену')
    def change_price(modeladmin, request, queryset):
        queryset.update(price=F('price') * 1.1)

    @admin.action(description="Сбросить количество в ноль")
    def reset_quantity(modeladmin, request, queryset):
        queryset.update(product_amount=0)

    list_display = ['product_name', 'description', 'price', 'product_amount', 'product_reg_date']
    search_fields = ['product_name']
    search_help_text = 'Поиск по полю Название товара (PRODUCT NAME)'
    ordering = ['-price']
    list_filter = ['product_reg_date', 'product_amount', 'price']
    actions = [change_price, reset_quantity]
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['product_name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Цена товара и его количество',
                'fields': ['price', 'product_amount'],
            },
        ),
        (
            'Описание товара',
            {
                'description': 'Описание товара',
                'fields': ['description'],
            }
        ),
    ]




class StoreOrder(admin.ModelAdmin):

    @admin.action(description='Отметить как выполненный')
    def mark_as_completed(modeladmin, request, queryset):
        queryset.update(status='completed')

    list_display = ['id', 'client_id', 'total_price', 'date_ordered', 'status']
    search_fields = ['date_ordered']
    search_help_text = 'Поиск по полю Дата регистрации заказа (PRODUCT NAME)'
    ordering = ['-total_price']
    list_filter = ['date_ordered']
    actions = [mark_as_completed]
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['client_id'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'ID товара и общая стоимость заказа',
                'fields': ['product_id', 'total_price'],
            },
        ),
        (
            'Статус заказа',
            {
                'description': 'Статус заказа',
                'fields': ['status'],
            }
        ),
    ]


admin.site.register(Client, StoreClient)
admin.site.register(Product, StoreProduct)
admin.site.register(Order, StoreOrder)
