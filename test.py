from time import sleep

import sys
from xcoin_api_client1 import *
from key import api_key, api_secret

api = XCoinAPI(api_key, api_secret)

while True:
    rgParams = {
        'endpoint': '/info/order_detail', 
        "order_id": 'C0101000001242707453',
        "order_currency": "BTC",
        "payment_currency": "KRW"
    }
    sleep(0.01)
    result = api.xcoinApiCall(rgParams['endpoint'], rgParams)
    try:
        price = int(result['data']['contract'][0]['price']) # 매수 체결가 
        if price > 1:
            break
    except IndexError:
        continue

print(price)