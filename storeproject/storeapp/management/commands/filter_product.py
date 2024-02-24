from django.core.management.base import BaseCommand
from storeapp.models import Product


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        try:
            product = Product.objects.get(pk=1)
            self.stdout.write(f'Название: {product.product_name}, Описание: {product.description}, '
                              f'Цена: {product.price}, Количество: {product.product_amount}, '
                              f'Дата регистрации: {product.product_reg_date}')
        except Product.DoesNotExist:
            self.stdout.write('Товара с таким ID не существует')
