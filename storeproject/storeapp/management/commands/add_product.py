from django.core.management.base import BaseCommand
from storeapp.models import Product
from random import choice, randint


class Command(BaseCommand):
    help = "Add product."

    def add_arguments(self, parser):
        parser.add_argument('num_products', type=int, help='Количество товаров для добавления')

    def handle(self, *args, **kwargs):
        amount = kwargs['num_products']
        for _ in range(amount):
            product = Product(
                product_name=choice(["Ботинки", "Кроссовки", "Сандали", "Тапочки", "Туфли", "Джинсы", "Куртка", "Брюки"]),
                description=f'{choice(["мужские", "женские", "унисекс"])}, {choice(["черный", "красный", "синий"])}',
                price=randint(1000, 10000),
                product_amount=randint(10, 100)
            )
            product.save()

