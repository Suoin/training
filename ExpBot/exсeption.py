import requests
import json
from config import keys

# Обработчик ошибок пользователя и запрос к апи
class ConvertException(Exception):
    pass
class ValuteConvert:
    @staticmethod
    def convert(quote: str, base: str, amount:str):

        if quote == base:
            raise ConvertException(f'Нельзя переводить одинаковые валюты {base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertException(f'Не доступная валюта {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertException(f'Не доступная валюта {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertException(f'Не верно задано количество {amount}')
        r = requests.get(f'https://v6.exchangerate-api.com/v6/2c4a11f9a43f67a82a7d2f8f/pair/{quote_ticker}/{base_ticker}/{amount}')
        total = json.loads(r.content)['conversion_result']
        price = json.loads(r.content)['conversion_rate']
        return total, price