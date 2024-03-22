from time import sleep
from xcoin_api_client1 import *
import sys
from key import api_key_withdraw, api_secret_withdraw
from key import ko_name, en_name

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

upbit_sol_address = {
    "address": "DajThCX3PGn17SUvR7MRMjCNmNpk6m7qpTBbY13QLN9P",
    "exchange_name": "UPBIT"
}

def bithumb_api_query(endpoint, payload):
    api = XCoinAPI(API_KEY, API_SECRET)
    rgParams = {
        'endpoint': endpoint  #<-- endpoint가 가장 처음으로 와야 한다.
    }

    rgParams.update(payload) # dictionary merge

    result = api.xcoinApiCall(rgParams['endpoint'], rgParams)
    return result

def get_available(currency):
    currency = currency.lower() # for dictionary key
    endpoint = '/info/balance'
    payload =  { "currency": currency }
    response = bithumb_api_query(endpoint, payload)
    available_usdt = response['data'][f'available_{currency}']
    return available_usdt


def withdraw_usdt(units, address, currency="USDT"):
    endpoint = '/trade/btc_withdrawal'
    payload = {
    "cust_type_cd": "01",
    "units": units,
    "address": address["address"],
    "currency": currency,
    "ko_name": ko_name,
    "en_name": en_name,
    "exchange_name": address["exchange_name"]
    }
    response = bithumb_api_query(endpoint, payload)
    print(response)
    status = response['status']
    if status == "0000":
        print(f"withdraw {units} {currency} success !!")
    return status


while True:
    currency = "SOL"
    available_sol = get_available(currency)
    print(f"now available currency: {available_sol} {currency}")
    sleep(5)
    if float(available_sol) > 61:
        status = withdraw_usdt(available_sol, upbit_sol_address, currency)
        if status == "0000":
            sys.exit(1)


'''
available_usdt = get_available("USDT")
print(f"now available usdt: {available_usdt}")

input()
# withdraw_usdt(available_usdt, binance_adddress)

while True:
    usdt_balance = get_available("USDT")
    sleep(1)

    print(f"now available usdt balance: {usdt_balance}")

    if float(usdt_balance) > 20000:
        withdraw_usdt(available_usdt, binance_adddress)
        sys.exit(0)

'''