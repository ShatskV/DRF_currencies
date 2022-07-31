from currency.models import Currency
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'change rate currency'

    def add_arguments(self, parser):
        parser.add_argument('charcode', help='Код валюты')
        parser.add_argument('rate', type=float, help='Курс валюты')

    def handle(self, *args, **kwargs):
        charcode = kwargs['charcode']
        rate = kwargs['rate']
        if not(charcode and rate):
            print('Не хватает аргументов!')
            return
        currency = Currency.objects.filter(charcode=charcode).first()
        if not currency:
            print('Такой валюты нет в базе!')
            return
        currency.rate = rate
        currency.save()
