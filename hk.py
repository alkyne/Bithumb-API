from time import sleep

import sys
from xcoin_api_client1 import *
from datetime import datetime

api_key = "API KEY"
api_secret = " API SECRET"

interval = 0.05

api = XCoinAPI(api_key, api_secret)

# hard coding version
buy_quantity = 0.005 # about 300,000 KRW

print (f"buy_quantity: {buy_quantity}")
input("Press Enter key to proceed")

total_trade_krw = 0

cnt = 100000
while cnt >= 0:
    cnt = cnt - 1
    try:
       
        # bid (market)
        ########################################################################

        rgParams = {
            'endpoint': '/trade/market_buy',  #<-- endpoint가 가장 처음으로 와야 한다.
            "units": buy_quantity,
            "order_currency": "BTC",
            "payment_currency": "KRW"
        }

        result = api.xcoinApiCall(rgParams['endpoint'], rgParams)
        print(f"매수 주문: {result}")
        total_trade_krw = total_trade_krw + (buy_quantity * current_price)

        sleep(0.02)

        # ask (market)
        ########################################################################

        # 매수한 양만큼 전부 시장가 매도
        rgParams = {
            'endpoint': '/trade/market_sell',  #<-- endpoint가 가장 처음으로 와야 한다.
            "units": buy_quantity,
            "order_currency": "BTC",
            "payment_currency": "KRW"
        }
        result = api.xcoinApiCall(rgParams['endpoint'], rgParams)

        ########################################################################

        print(f"매도 주문: {result}")
        total_trade_krw = int(total_trade_krw + (buy_quantity * current_price))

        print(f"Total trade KRW: {format(total_trade_krw, ',')}")
        print()

        if total_trade_krw >= 500000000:
            break

        sleep(interval)

    except Exception as e:
        print(f"에러 발생: {e}")
        sleep(interval)