from time import sleep
from xcoin_api_client1 import *
import sys
from key import api_key_withdraw, api_secret_withdraw

API_KEY = api_key_withdraw
API_SECRET = api_secret_withdraw

binance_adddress = {
    "address": "TLKffTYd5rPqbj7rKzAEoWQW4UPf4BXyZW",
    "exchange_name": "BINANCE"
}

bybit_address = {
    "address": "TGcE9F5sWFKjTgLL1cQYtHy8E8tTkZKvDi",
    "exchange_name": "BYBIT"
}

def bithumb_api_query(endpoint, payload):
    api = XCoinAPI(API_KEY, API_SECRET)
    rgParams = {
        'endpoint': endpoint  #<-- endpoint가 가장 처음으로 와야 한다.
    }

    rgParams.update(payload) # dictionary merge

    result = api.xcoinApiCall(rgParams['endpoint'], rgParams)
    return result

def get_available_usdt():
    
    endpoint = '/info/balance'
    payload =  { "currency": "USDT" }
    response = bithumb_api_query(endpoint, payload)
    available_usdt = response['data']['available_usdt']
    return available_usdt


def withdraw_usdt(units, address):
    endpoint = '/trade/btc_withdrawal'
    payload = {
    "cust_type_cd": "01",
    "units": units,
    "address": address["address"],
    "currency": "USDT",
    "ko_name": "최동민",
    "en_name": "DONGMIN CHOI",
    "exchange_name": address["exchange_name"]
    }
    response = bithumb_api_query(endpoint, payload)
    print(response)
    currency = "USDT"
    if response['status'] == "0000":
        print(f"withdraw {units} {currency} success !!")
    return response

available_usdt = get_available_usdt()
print(f"now available usdt: {available_usdt}")

input()
withdraw_usdt(available_usdt, bybit_address)

# while True:
#     usdt_balance = get_available_usdt()
#     sleep(1)

#     print(f"now available usdt balance: {usdt_balance}")

#     if float(usdt_balance) > 21000:
#         withdraw_usdt(usdt_balance, addr, exchange_name)
#         sys.exit(0)