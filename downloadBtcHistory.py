import requests
import datetime
import os
import pandas as pd


# def daily_price_historical(symbol, comparison_symbol, exchange='', allData='true'):
#     url = 'https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym={}&allData={}' \
#         .format(symbol.upper(), comparison_symbol.upper(), allData)
#     if exchange:
#         url += '&e={}'.format(exchange)
#     page = requests.get(url)
#     data = page.json()['Data']
#     df = pd.DataFrame(data)
#     if hasattr(df, 'time'):
#         df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
#     return df


def hourly_price_historical(symbol, comparison_symbol, exchange='', limit='8000'):
    url = 'https://min-api.cryptocompare.com/data/histohour?fsym={}&tsym={}&limit={}' \
        .format(symbol.upper(), comparison_symbol.upper(), limit)
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()['Data']
    df = pd.DataFrame(data)
    if hasattr(df, 'time'):
        df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
    return df


def get_exchanges():
    url = 'https://min-api.cryptocompare.com/data/all/exchanges'
    page = requests.get(url)
    data = page.json()
    df = pd.DataFrame(data)
    return df


exchanges = get_exchanges()

for exchange_name in exchanges:
    print(exchange_name)
#    history = daily_price_historical('BTC', 'USD', exchange_name)
    history = hourly_price_historical('BTC', 'USD', exchange_name)
    history.to_csv(os.getcwd()+'/exchange_history/' + exchange_name + '.csv')
