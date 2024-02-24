from django.core.management.base import BaseCommand
from storeapp.models import Order


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        try:
            order = Order.objects.filter(pk=4).first()
            order.total_price = 17600
            order.product_id.set([1, 4, 14])
            order.date_ordered = '2023-01-11 14:41:09'
            order.save()
            self.stdout.write('Данные заказа успешно обновлены')
        except Order.DoesNotExist:
            self.stdout.write(f'Заказа с таким ID не существует')



