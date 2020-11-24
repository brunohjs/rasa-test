import requests
from helpers import constants

API_URL = 'https://economia.awesomeapi.com.br'

def getAllExchangeRates():
    result = requests.get('{}/json/all'.format(API_URL))
    if result.status_code == 200:
        data = dict()
        availableCurrencies = {item[1]['code']: item[0] for item in constants.currencies.items()}
        for item in result.json().values():
            if item['code'] in availableCurrencies:
                data[availableCurrencies[item['code']]] = {
                    "code": item['code'],
                    "name": item['name'],
                    "high": item['high'],
                    "low": item['low'],
                    "value": item['bid'],
                    "time": item['create_date']
                }
        return response(result.status_code, data)
    return response(result.status_code, result.json())

def getExchangeRate(currencyCode):
    params = '{}-BRL'.format(currencyCode)
    result = requests.get('{}/json/all/{}'.format(API_URL, params))
    return response(result.status_code, result.json())

def response(status_code, data={}):
    error = False
    if status_code >= 400:
        error = True
    return {
        "error": error,
        "statusCode": status_code,
        "data": data
    }
