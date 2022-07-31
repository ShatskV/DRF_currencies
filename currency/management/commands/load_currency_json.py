import json

from currency.models import Currency
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Load currencies from json'

    def add_arguments(self, parser):
        parser.add_argument('-p','--path', type=str, help="Путь до файла .json, default: 'currency.json'", default='currency.json')

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'r') as file:
            currencies = json.load(file)
        
        valute = currencies.get('Valute')
        if not valute:
            print('No valute data!')
        for currency in valute.values():
            charcode = currency.get('CharCode')
            nominal = currency.get('Nominal')
            rate = currency.get('Value')
            name = currency.get('Name')
            if all([charcode, nominal, rate, name]):
                Currency.objects.update_or_create(name=name,
                                                  rate=rate,
                                                  charcode=charcode,
                                                  nominal=nominal)
            else:
                print('Отсутсвуют необходимые поля для валюты!')
        

