from django.core.management.base import BaseCommand
from storeapp.models import Client


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        try:
            client = Client.objects.get(pk=20)
            self.stdout.write(f'Клиент: {client.name}, Email: {client.email}, '
                              f'Телефон: {client.phone_number}, Адрес: {client.address}, '
                              f'Дата регистрации: {client.registration_date}')
        except Client.DoesNotExist:
            self.stdout.write('Клиента с таким ID не существует')
