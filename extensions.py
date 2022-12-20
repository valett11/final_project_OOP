import json
import requests
from config import keys

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Не удалось перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}.')

        try:
            amount = float(amount)
        except KeyError:
            raise ConvertionException(f'Не удалось обработать количество {amount}.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')

        total_base = json.loads(r.content)[keys[quote]] * amount

        return total_base