from time import sleep

import sys
from xcoin_api_client1 import *
from key import api_key, api_secret
from datetime import datetime
# from utils import calc_pnl

# 매수 거래 id, 매도 거래 id
def calc_pnl(bid_order_id, ask_order_id, quantity):
    bid_price = _get_price_from_order_id(bid_order_id)
    ask_price = _get_price_from_order_id(ask_order_id)

    pnl = round(ask_price * quantity) - round(bid_price * quantity)
    return pnl

def _get_price_from_order_id(order_id):
    api = XCoinAPI(api_key, api_secret)
    while True:
        rgParams = {
            'endpoint': '/info/order_detail', 
            "order_id": order_id,
            "order_currency": "BTC",
            "payment_currency": "KRW"
        }
        result = api.xcoinApiCall(rgParams['endpoint'], rgParams)
        try:
            price = int(result['data']['contract'][0]['price']) # 매수 체결가 
            if price > 1:
                return price
        except IndexError:
            # print("Getting price order_id...")
            sleep(0.01)
            continue


# for debugging
if __name__ == '__main__':
    bid_order_id = 'C0101000001315044823'
    ask_order_id = 'C0101000001315045018'
    pnl = calc_pnl(bid_order_id, ask_order_id, 0.0034)

    print(type(pnl))