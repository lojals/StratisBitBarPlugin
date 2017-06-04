#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# <bitbar.title>Stratis rates in USD</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Jorge Ovalle</bitbar.author>
# <bitbar.author.github>lojals</bitbar.author.github>
# <bitbar.desc>Displays Stratis info from coinmarketcap</bitbar.desc>
# <bitbar.image>https://cloud.githubusercontent.com/assets/6756995/26758031/90dacdda-4897-11e7-94f2-3efdda119746.png</bitbar.image>
# <bitbar.dependencies>python</bitbar.dependencies>
# <bitbar.abouturl>https://github.com/lojals/StratisBitBarPlugin</bitbar.abouturl>
#

from urllib import urlopen
url = urlopen('https://api.coinmarketcap.com/v1/ticker/stratis/').read()


import json
result = json.loads(url)

def render():
    priceUSD = float(result[0]['price_usd'])
    priceBTC = float(result[0]['price_btc'])
    image = ''
    
    if result[0]['percent_change_24h'] > '0':
        image = 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QAyQACAALwzISXAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4AQHACkSBTjB+AAAALNJREFUOMvVk70NAjEMhb87WYiGBZAQU7ABNSVSWpZgEEagsJDoKBELUCEKFuBuCKTw0xyQC0lICe5i+/k9/wT+3opUUJQhcAUqa8I5ZQT4tANwioGTCkQZA9vmOQE2oUJFhL0DXBz33RpKUfCLfLTQJMx9IlEWuQr6QB3prGtNS1lwiMvEYo7ekNsKRBkB+y+rH1hDFVOwy7ids+gbVzrsM6CXeYDTF85xroB1ZoHb73ymB5RhJkpZTihGAAAAAElFTkSuQmCC'
    else:
        image = 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QABACnAADQ9FZaAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4AQHACQ1FZwK3gAAAMRJREFUOMvNkjEKAjEQRZ+jKNjYKh5AbzCdjVcQj+BFPIKlp7EMeAJrUbASQVCEr80uG9cNbqe/Cgn/5WUI/DqNfBHM+kCzbs+lPUAr2pwBq5qABbB+M8gszkDvS/kOdAG5VBgEM4ApsP0CGLukjxlEoA0wSZR3Lo0qhxhZDIBDAmDA0wsBLD51CZeOwLKivHbprZx6AkAHuEXbD5fawYwywMqAzOKeDTTPvKqcTGZBMLsGs0utn5gADYEHcKp9e9ni//MCDtNCE3qjsIwAAAAASUVORK5CYII='
    
    print ('  %.3f USD | image=%s'% (priceUSD, image))
    print ('  %.5f BTC | image=%s'% (priceBTC, image))
    print('Rank: %s' % result[0]['rank'])

render()
