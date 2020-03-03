#!/usr/bin/env python3

import configparser
import sys
from requests import Request, Session
from requests.exceptions import Timeout, TooManyRedirects
import json

configuration = configparser.ConfigParser()

with open('stonks-config.ini', 'r', encoding='utf-8') as f:
    configuration.read_file(f)

config = configuration['general']
currencies = config['coins']
base_currency = config['base_currency']
APIKey = config['APIKey']
display = config['display']
decimalpoints = int(config['decimalpoints'])

# currencies = (config['general']['coins'])
# base_currency = config['general']['base_currency']
# APIKey = config['general']['APIKey']
# display = config['general']['display']
# decimalpoints = config['general']['decimalpoints']

if display == 'percent' or display == 'both':
    percents = True
    aliases = {'day': ['percent_change_24h', '24h'],
            'week': ['percent_change_7d', '7d'],
            'hour': ['percent_change_1h', '1h']}
    options = config['percentchg'].split(',')
    percentchg = [aliases[i] for i in options]

# API call
params= {'convert': base_currency,
        'symbol': currencies}
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
headers = {'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': APIKey}
session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=params)
    data = json.loads(response.text)['data']
    for currency in currencies.split(','):
        local_price = data[currency]['quote'][base_currency]['price']
        local_price = round(float(local_price), decimalpoints)
        sys.stdout.write(f'[{currency}] {local_price} ')
        if percents == True: 
            for opt in percentchg:
                val = opt[0]
                change = data[currency]['quote'][base_currency][val]
                change = round(float(change), 2)
                sys.stdout.write(f'{opt[1]}: {change}% ')

except (ConnectionError, Timeout, TooManyRedirects) as e:
    sys.stdout.write(e)

