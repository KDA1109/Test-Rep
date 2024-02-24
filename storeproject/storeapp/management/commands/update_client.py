from django.core.management.base import BaseCommand
from storeapp.models import Client


class Command(BaseCommand):

    def handle(self, *args, **kwargs):


        try:
            client = Client.objects.get(pk=9)
            client.name = 'Петр'
            client.email = 'petr@mail.ru'
            client.phone_number = '+79261234567'
            client.address = 'address'
            client.save()
            self.stdout.write('Данные клиента успешно обновлены')
        except Client.DoesNotExist:
            self.stdout.write(f'Клиента с таким ID не существует')



