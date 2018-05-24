from zeep import Client
from file_utils import parse_records

TEMP_SERVICE_URL = 'https://www.w3schools.com/xml/tempconvert.asmx?WSDL'


def get_avg_temp(source_file):
    source_temps = [int(row[0]) for row in parse_records(source_file)]
    average_temperature = sum(source_temps) / len(source_temps)

    return '{0:.1f}'.format(convert_fahrenheit_to_celsius(average_temperature))


def convert_fahrenheit_to_celsius(source_temp):
    client = Client(TEMP_SERVICE_URL)
    return float(client.service.FahrenheitToCelsius(source_temp))


print('Average temperature is {} degree Celsius'.format(get_avg_temp('sources/temps.txt')))
