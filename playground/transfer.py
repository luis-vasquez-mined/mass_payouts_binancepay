import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage

import os
from signature import send_signed_request
from pandas import read_excel
from uuid import uuid4
import pandas as pd
from openpyxl import Workbook
from datetime import date
import time

from config import DEBUG
#
import random
#

# Balance
# POST /binancepay/openapi/balance
#


def balance(wallet):
    response = send_signed_request(
        'POST',
        '/binancepay/openapi/balance',
        {
            "wallet": wallet,
            "currency": "USDT"
        },
    )
    # print(response)
    return response['data']['balance']

# Transfer
# POST /binancepay/openapi/wallet/transfer


def transfer(request_id, currency, amount, transferType):
    if DEBUG == True:
        return {
            "status": "SUCCESS",
            "code": "000000",
            "data": {
                "tranId": "100002021071407140001",
                "status": "SUCCESS",
                "currency": "BNB",
                "amount": "0.01",
                "transferType": "TO_MAIN"
            },
            "errorMessage": ""
        }

    response = send_signed_request(
        'POST',
        '/binancepay/openapi/wallet/transfer',
        {
            "requestId": request_id,
            "currency": currency,
            "amount": amount,
            "transferType": transferType
        },
    )
    return response


def test(request_id, currency, amount, transferType):
    print(
        f"Estas enviando los datos de {request_id}, {currency}, {amount}, {transferType}")
    random_number = random.randint(1, 2)
    status = ''
    if (random_number == 1):
        status = "SUCCESS"
    else:
        status = "FAIL"
    data = {"status": status}
    return data

    # return response


# balance_funding = balance("FUNDING_WALLET")
# balance_spot = balance("SPOT_WALLET")

# print(balance_funding)
# print(balance_spot)
# print()

# ###

# response = transfer("transfer_18-12-2023_prod1", "USDT", 0.00, "TO_MAIN")
# print(response)
# print()

# time.sleep(20)

# balance_funding = balance("FUNDING_WALLET")
# balance_spot = balance("SPOT_WALLET")
# print(balance_funding)
# print(balance_spot)
# print()
