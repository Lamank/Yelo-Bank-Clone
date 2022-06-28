
import requests
import xmltodict
from datetime import date
today = date.today().strftime("%d.%m.%Y")

response = requests.get(f'https://www.cbar.az/currencies/{today}.xml')
data = xmltodict.parse(response.text)
# print(data)
exchange = []


for i in data['ValCurs']['ValType']:
    for x in i['Valute']:
        if x['@Code'] == 'USD' or x['@Code'] == 'EUR':
            exchange.append(x)
# print(exchange)

    
# export FLASK_ENV=development
# git push --set-upstream origin ＜laman＞ 
# flask db stamp head             



