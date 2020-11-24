from datetime import datetime
from pytz import timezone
from helpers.constants import currencies
from services.exchangeRateService import getAllExchangeRates

def filterEntities(entities, entityName):
    if isinstance(entityName, str):
        return list(filter(lambda entity: entity['entity'] == entityName, entities))
    else:
        return list(filter(lambda entity: entity['entity'] in entityName, entities))

def showCurrencyList():
    message = 'Esses são as moedas que conheço:\n\n'
    copyCurrencies = currencies.copy()
    copyCurrencies = list(copyCurrencies.values())
    for currency in copyCurrencies:
        message += '  • {} ({})\n\n'.format(currency['name'], currency['symbol'])
    return message

def showCurrencyPrice():
    copyCurrencies = currencies.copy()
    message = 'A cotação do Real é:\n\n'
    result = getAllExchangeRates()
    if result['statusCode'] == 200:
        time = ''
        for item in result['data'].items():
            new_time = datetime.strptime(item[1]['time'], '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone('America/Sao_Paulo'))
            last_update = int((datetime.now(timezone('America/Sao_Paulo')) - new_time).total_seconds() / 60)
            if not time:
                time = new_time
            if time < new_time:
                time = new_time
            data = copyCurrencies[item[0]]
            data['value'] = item[1]['value']
            message += '  • {:15} ({}): → R$ {}\n\n'.format(data['name'], data['symbol'], formatMoney(data['value']))
        if last_update > 1:
            last_update_message = '{} minutos'.format(last_update)
        elif last_update == 1:
            last_update_message = '1 minuto'
        else:
            last_update_message = 'poucos segundos'
        message += 'Última atualização: há {}'.format(last_update_message)
        return message
    else:
        return 'Houve algum problema para encontrar a cotação. Tente novamente mais tarde.'

def showConversions(entities):
    copyCurrencies = currencies.copy()
    values = filterEntities(entities, ['number', 'amount-of-money'])
    try:
        for i in range(len(values)):
            if isinstance(values[i]['value'], str):
                values[i] = float(values[i]['value'].replace(',', '.'))
            else:
                values[i] = values[i]['value']
    except ValueError:
        values = []
    exchange_rates = getAllExchangeRates()
    if exchange_rates['statusCode'] == 200:
        last_update = -1
        message = ''
        time = ''
        if len(values) == 0:
            return 'Não consegui identificar valores para fazer a conversão. Poderia tentar novamente?'
        for value in values:
            if value > 0:
                message += 'A conversão de R$ %s é:\n\n' % (formatMoney(value))
                for exchange_rate in exchange_rates['data'].items():
                    new_time = datetime.strptime(exchange_rate[1]['time'], '%Y-%m-%d %H:%M:%S')
                    last_update = int((datetime.now() - new_time).total_seconds() / 60)
                    if not time:
                        time = new_time
                    if time < new_time:
                        time = new_time
                    converted_value = formatMoney(value / float(exchange_rate[1]['value'].replace(',', '.')))
                    currency = copyCurrencies[exchange_rate[0]]
                    message += '  • {:15} → {} {} ({})\n\n'.format(currency['name'], currency['symbol'], converted_value, formatMoney(exchange_rate[1]['value']))
            else:
                message += 'O valor tem que ser maior que zero. Você informou um valor inválido: %.2f.\n\n' % (value)
        if last_update > 1:
            message += 'Última atualização: há {} minutos'.format(last_update)
        elif last_update == 1:
            message += 'Última atualização: há 1 minuto'
        elif last_update == 0:
            message += 'Última atualização: há poucos segundos'
        return message
    else:
        return 'Houve algum problema para encontrar a cotação. Tente novamente mais tarde.'

def formatMoney(value):
    value = float(value.replace(',', '.')) if isinstance(value, str) else float(value)
    value = str(round(value, 2))
    split = value.split('.')
    intValue = value.split('.')[0]
    aux = ''
    if len(intValue) > 3:
        intValue = intValue[::-1]
        for i in range(0, len(intValue), 3):
            aux += intValue[i:i + 3] + '.' if i + 3 < len(intValue) else intValue[i:i + 3]
        aux = aux[::-1]
        intValue = aux
    if len(split) == 2:
        floatValue = value.split('.')[1]
        if len(floatValue) == 1:
            floatValue += '0'
        return '{},{}'.format(intValue, floatValue)
    else:
        return '{},00'.format(intValue)

def log(message):
    date = datetime.now(timezone('America/Sao_Paulo')).replace(microsecond=0).isoformat()
    print('[{}][{}]{} > {}'.format(
        date,
        (message['intent']['name'], '%.2f' % (message['intent']['confidence'])),
        [(item['entity'], item['value']) for item in message['entities']] if message['entities'] else '[-]',
        message['text']
    ))
