import math
from zeep import Client
from file_utils import parse_records

CURRENCY_SERVICE_URL = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'


def count_expenses(currencies_file):
    currencies = parse_records(currencies_file)

    converted = [convert_currency(record[1], record[2]) for record in currencies]
    return math.ceil(sum(converted))


def convert_currency(amount, source_currency, target_currency='RUB'):
    client = Client(CURRENCY_SERVICE_URL)
    result = client.service.ConvertToNum(fromCurrency=source_currency, toCurrency=target_currency, amount=amount, rounding=True)
    print('Converted {} {} to {}, result: {}'.format(amount, source_currency, target_currency, result))
    return result

print('\nTotal amount is {} RUB'.format(count_expenses('sources/currencies.txt')))
