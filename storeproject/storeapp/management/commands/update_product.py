from django.core.management.base import BaseCommand
from storeapp.models import Product


class Command(BaseCommand):

    def handle(self, *args, **kwargs):


        try:
            product = Product.objects.get(pk=27)
            product.foto = '100050174928b0.jpg'
            product.save()
            self.stdout.write('Данные товара успешно обновлены')
        except Product.DoesNotExist:
            self.stdout.write(f'Товара с таким ID не существует')



