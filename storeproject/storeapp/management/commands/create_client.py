from django.core.management.base import BaseCommand
from storeapp.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(
            name='Иван',
            email='vanya@mail.ru',
            phone_number='+79261234570',
            address='address'
        )
        client.save()

