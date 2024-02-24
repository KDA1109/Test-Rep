from django.core.management.base import BaseCommand
from storeapp.models import Order, Client, Product
from random import choice, randint

class Command(BaseCommand):
    help = "Добавление заказов."

    def add_arguments(self, parser):
        parser.add_argument('num_orders', type=int, help='Количество заказов для добавления')

    def handle(self, *args, **kwargs):
        num_orders = kwargs['num_orders']

        clients = Client.objects.all()
        products = Product.objects.all()

        for _ in range(num_orders):
            rnd_client = choice(clients)
            num_items = randint(1, 5)

            # Создаем заказ
            order = Order.objects.create(
                total_price=0,
                client_id=rnd_client,
            )

            # Добавляем случайные товары в заказ
            for _ in range(num_items):
                rnd_product = choice(products)
                amount = randint(1, 5)

                # Добавляем товар в заказ
                order.product_id.add(rnd_product)

                # Обновляем общую стоимость заказа
                order.total_price += rnd_product.price * amount

            order.save()

        print(f"Добавлено {num_orders} заказов в базу данных.")
