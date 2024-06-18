from signature import send_signed_request
from config import DEBUG


class FontType:
    FONT_14 = ("Arial", 14)
    FONT_16 = ("Arial", 16)


class TransactionType:
    PAYMENT = "Payment"
    PAYOUT = "Payout"


class WalletType:
    FUNDING_WALLET = "FUNDING_WALLET"
    SPOT_WALLET = "SPOT_WALLET"


# Balance v1
# POST /binancepay/openapi/balance

def balancev1(wallet):
    if DEBUG == True:
        return {
            "status": "SUCCESS",
            "code": "000000",
            "data": {
                "balance": 99999.0001,
                "asset": "USDT",
                "fiat": "USD",
                "availableFiatValuation": 138049.59970654,
                "availableBtcValuation": 3.00872499
            }
        }

    response = send_signed_request(
        'POST',
        '/binancepay/openapi/balance',
        {
            "wallet": wallet,
            "currency": "USDT"
        },
    )
    return response

# Balance v2
# POST /binancepay/openapi/v2/balance


def balancev2(wallet):
    if DEBUG == True:
        if wallet == WalletType.FUNDING_WALLET:
            return {
                "status": "SUCCESS",
                "code": "000000",
                "data": {
                    "balance": [
                        {
                            "available": 99999.0001,
                            "freeze": 0.0,
                            "asset": "USDT",
                            "availableFiatValuation": 15649.11989303,
                            "availableBtcValuation": 0.34092465
                        }
                    ],
                    "wallet": "FUNDING_WALLET",
                    "updateTime": 1704924149796,
                    "fiat": "USD"
                }
            }
        elif wallet == WalletType.SPOT_WALLET:
            return {
                "status": "SUCCESS",
                "code": "000000",
                "data": {
                    "balance": [
                        {
                            "available": 99999.0002,
                            "freeze": 0.0,
                            "asset": "BNB",
                            "availableFiatValuation": 0.0,
                            "availableBtcValuation": 0.0
                        },
                        {
                            "available": 0.0,
                            "freeze": 0.0,
                            "asset": "BTC",
                            "availableFiatValuation": 0.0,
                            "availableBtcValuation": 0.0
                        },
                        {
                            "available": 0.0,
                            "freeze": 0.0,
                            "asset": "BUSD",
                            "availableFiatValuation": 0.0,
                            "availableBtcValuation": 0.0
                        },
                        {
                            "available": 0.87821465,
                            "freeze": 0.0,
                            "asset": "LDBTC",
                            "availableFiatValuation": 0.0,
                            "availableBtcValuation": 0.0
                        },
                        {
                            "available": 0.0,
                            "freeze": 0.0,
                            "asset": "LDBUSD",
                            "availableFiatValuation": 0.0,
                            "availableBtcValuation": 0.0
                        },
                        {
                            "available": 1314.80755284,
                            "freeze": 0.0,
                            "asset": "LDMATIC",
                            "availableFiatValuation": 0.0,
                            "availableBtcValuation": 0.0
                        },
                        {
                            "available": 93535.54808372,
                            "freeze": 0.0,
                            "asset": "LDUSDC",
                            "availableFiatValuation": 0.0,
                            "availableBtcValuation": 0.0
                        },
                        {
                            "available": 175063.40979137,
                            "freeze": 0.0,
                            "asset": "LDUSDT",
                            "availableFiatValuation": 0.0,
                            "availableBtcValuation": 0.0
                        },
                        {
                            "available": 0.0,
                            "freeze": 0.0,
                            "asset": "MATIC",
                            "availableFiatValuation": 0.0,
                            "availableBtcValuation": 0.0
                        },
                        {
                            "available": 0.0,
                            "freeze": 0.0,
                            "asset": "USDC",
                            "availableFiatValuation": 0.0,
                            "availableBtcValuation": 0.0
                        },
                        {
                            "available": 138049.599741,
                            "freeze": 0.0,
                            "asset": "USDT",
                            "availableFiatValuation": 138049.59973578,
                            "availableBtcValuation": 3.00492586
                        }
                    ],
                    "wallet": "SPOT_WALLET",
                    "updateTime": 1704924150988,
                    "fiat": "USD"
                }
            }

    response = send_signed_request(
        'POST',
        '/binancepay/openapi/v2/balance',
        {
            "wallet": wallet,
        },
    )
    return response

# Payout Validate Receiver
# POST /binancepay/openapi/payout/receiver/check


def verification(pay_id):
    if DEBUG == True:
        return {
            "status": "SUCCESS",
            "code": "000000",
            "data": True
        }

    response = send_signed_request(
        'POST',
        '/binancepay/openapi/payout/receiver/check',
        {
            "receiveType": "PAY_ID",  # enum : {PAY_ID, BINANCE_ID}
            "receiverId": pay_id,
        }
    )
    return response

# Payment Payer Verification
# POST /binancepay/openapi/order/payer/verification


def ppverification(pay_id, first_name, last_name):
    response = send_signed_request(
        'POST',
        '/binancepay/openapi/order/payer/verification',
        {
            "payerType": "INDIVIDUAL",
            "accountId": pay_id,
            "information": [
                {
                    "category": "FIRST_NAME",
                    "value": first_name,
                },
                {
                    "category": "LAST_NAME",
                    "value": last_name,
                }
            ]
        }
    )
    return response

# Payout Query
# POST   /binancepay/openapi/payout/query


def query(id):
    response = send_signed_request(
        'POST',
        '/binancepay/openapi/payout/query',
        {
            "requestId": id,
        }
    )
    return response

# Payouts
# POST /binancepay/openapi/payout/transfer


def payout(amount, id, receive_type, receiver):
    if DEBUG == True:
        return {
            "status": "SUCCESS",
            "code": "000000",
            "data":
                {
                    "requestId": "samplerequest1234",
                    "status": "ACCEPTED"
                }
        }
    response = send_signed_request(
        'POST',
        '/binancepay/openapi/payout/transfer',
        {
            "requestId": id,
            "batchName": "testing cents",
            "currency": "USDT",
            "totalAmount": amount,
            "totalNumber": 1,
            "bizScene": "DIRECT_TRANSFER",
            "transferDetailList": [
                {
                    "merchantSendId": "receiver",
                    "transferMethod": "SPOT_WALLET",
                    "transferAmount": amount,
                    "receiveType": receive_type,
                    "receiver": receiver,
                    "remark": "test1"
                }
            ]
        }
    )
    return response

# Extract balance


def extract_balance_v1(wallet):
    response = balancev1(wallet)
    return response['data']['balance']

# Download Report
# POST /binancepay/openapi/report/get-file


def report(reportType, transactionType, startDate, endDate):
    if DEBUG == True:
        return {
            "status": "SUCCESS",
            "code": "000000",
            "data": [
                {
                    "reportType": "Transaction",
                    "transactionType": "Payout",
                    "transactionDate": "15/08/2023",
                    "fileName": "T_Payout_15082023.xlsx",
                    "downloadUrl": "https://tf-bin-prod-payment-merchant-admin.s3.ap-northeast-1.amazonaws.com/dailyReport/310903519/T_Payout_15082023.xlsx?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaDmFwLW5vcnRoZWFzdC0xIkcwRQIgEpAosy0seV2k2MBo2yi3yJOq%2FuhZuigX64JgZ7qycGQCIQCPoSN5OKyZgK9HnVwoHp9eXgbmMiC2%2FRqZT8%2BEsAK%2BxCqYBQgfEAAaDDM2OTA5NjQxOTE4NiIMBa%2FsDvUDy7FOlO70KvUElL3SCUgbbOWG7DuBynxF4WDd6YPVGamspM5SGeFe4ujTrrFnPIWl%2FjLJAKnEyw3hcj5snh3qD3Tz%2FMzRQSdaHXXcfRQzu1WaIP4h9JJfvohGgMilkR0mmiMUVyD0Du%2FR8WOYroZD6koiF8q9Ukm6%2BIDP4dGRE1OAnPzQw4%2FqJuq378RGPVYT6kE2loHXPJt0Yg627Oax2hbGtepJ4fF8HlivwXAkXlpKTzsf2T1mtulSlh2Io6WJcT%2FiYhnz6Dns77FgmtifHf6%2Fg5S6tvDlhz5sQDhwXN%2B%2FPML%2FVcNJPGdml7b2gn3Sk%2BehbxgT8zTey9Iy6A8fcWG0JVLDvrRqZi%2FwGyB1iMStpxFYJKh0w%2B%2F035dvv%2BbTNo0vahRysBXrl8sWoRFzHfiJvCWFRvdNuQKVC3OcTWpe8zZ18lM%2F6qPPG437HQeI4vXawUX2hK%2B8wOPEAmoHJWUb2uiSH7EVmCJebdTlbhA7GKPtV9ubROrDZGSO4Qbr7DkSMfPlACdAEItkUTT2QaJ5luGWL1C6ir2SGpu9asvjIzllsA9nNg9T0YXbbkbizPzh4kji0scbO2neke9IoHvr6OKuSnjoVkvO2tIrRGQ%2BTwvQsLrVHNpMzbqWk%2Bq8AAzJ%2F9oXpa2w2JDBylKwNfuPVEpyH7EtoHok1QX2ydC6iAJ7X4O8dmE5pgcF3meW8f2FqWktnWb8QjPoemGKl4yrREr9zN9eP1UGRbHHUBM990GL5NVWss%2F6hCPrSiXyimLS2aTNmt%2BfVzDMtHt6igiSeXdHWbm5UOojIE9KiIu1Iu0YUik4BNwrP%2FkfmC9kHMsFMBSFG7d8desTjGMwyKT8rAY6mwGT1na%2F0fJMDBYQYdef5p7DTAVtg91Js7k8QiXIZyqnJhr1uydYM0wEtzgqyeU7uNu0dKNPKtuiWghRvee6w4YkX7IvLxWzYQKAsvACJCc54TpjzSwnJ6mSHY0q5p67ibStZlQn7%2BaijGL5MQaW7lWabOUY0hZM8rH5Hb%2Fkp3vQV5jKSYdvmJaVoeUXtOfSNA6i7I2ek3AqnyYC1w%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240110T221332Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIAVL364M5ZNINEVMOX%2F20240110%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-Signature=e195c820ce2660682aa8a347414ab48b1762afdd3704206d33f21bfcfe5a53c8"
                },
                {
                    "reportType": "Transaction",
                    "transactionType": "Payout",
                    "transactionDate": "12/08/2023",
                    "fileName": "T_Payout_12082023.xlsx",
                    "downloadUrl": "https://tf-bin-prod-payment-merchant-admin.s3.ap-northeast-1.amazonaws.com/dailyReport/310903519/T_Payout_12082023.xlsx?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaDmFwLW5vcnRoZWFzdC0xIkcwRQIgEpAosy0seV2k2MBo2yi3yJOq%2FuhZuigX64JgZ7qycGQCIQCPoSN5OKyZgK9HnVwoHp9eXgbmMiC2%2FRqZT8%2BEsAK%2BxCqYBQgfEAAaDDM2OTA5NjQxOTE4NiIMBa%2FsDvUDy7FOlO70KvUElL3SCUgbbOWG7DuBynxF4WDd6YPVGamspM5SGeFe4ujTrrFnPIWl%2FjLJAKnEyw3hcj5snh3qD3Tz%2FMzRQSdaHXXcfRQzu1WaIP4h9JJfvohGgMilkR0mmiMUVyD0Du%2FR8WOYroZD6koiF8q9Ukm6%2BIDP4dGRE1OAnPzQw4%2FqJuq378RGPVYT6kE2loHXPJt0Yg627Oax2hbGtepJ4fF8HlivwXAkXlpKTzsf2T1mtulSlh2Io6WJcT%2FiYhnz6Dns77FgmtifHf6%2Fg5S6tvDlhz5sQDhwXN%2B%2FPML%2FVcNJPGdml7b2gn3Sk%2BehbxgT8zTey9Iy6A8fcWG0JVLDvrRqZi%2FwGyB1iMStpxFYJKh0w%2B%2F035dvv%2BbTNo0vahRysBXrl8sWoRFzHfiJvCWFRvdNuQKVC3OcTWpe8zZ18lM%2F6qPPG437HQeI4vXawUX2hK%2B8wOPEAmoHJWUb2uiSH7EVmCJebdTlbhA7GKPtV9ubROrDZGSO4Qbr7DkSMfPlACdAEItkUTT2QaJ5luGWL1C6ir2SGpu9asvjIzllsA9nNg9T0YXbbkbizPzh4kji0scbO2neke9IoHvr6OKuSnjoVkvO2tIrRGQ%2BTwvQsLrVHNpMzbqWk%2Bq8AAzJ%2F9oXpa2w2JDBylKwNfuPVEpyH7EtoHok1QX2ydC6iAJ7X4O8dmE5pgcF3meW8f2FqWktnWb8QjPoemGKl4yrREr9zN9eP1UGRbHHUBM990GL5NVWss%2F6hCPrSiXyimLS2aTNmt%2BfVzDMtHt6igiSeXdHWbm5UOojIE9KiIu1Iu0YUik4BNwrP%2FkfmC9kHMsFMBSFG7d8desTjGMwyKT8rAY6mwGT1na%2F0fJMDBYQYdef5p7DTAVtg91Js7k8QiXIZyqnJhr1uydYM0wEtzgqyeU7uNu0dKNPKtuiWghRvee6w4YkX7IvLxWzYQKAsvACJCc54TpjzSwnJ6mSHY0q5p67ibStZlQn7%2BaijGL5MQaW7lWabOUY0hZM8rH5Hb%2Fkp3vQV5jKSYdvmJaVoeUXtOfSNA6i7I2ek3AqnyYC1w%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240110T221332Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIAVL364M5ZNINEVMOX%2F20240110%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-Signature=75500b68127e9229aef5526fb4ccbb4d56eee34ddb36d8db73c33fb57f39a46c"
                },
                {
                    "reportType": "Transaction",
                    "transactionType": "Payout",
                    "transactionDate": "11/08/2023",
                    "fileName": "T_Payout_11082023.xlsx",
                    "downloadUrl": "https://tf-bin-prod-payment-merchant-admin.s3.ap-northeast-1.amazonaws.com/dailyReport/310903519/T_Payout_11082023.xlsx?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaDmFwLW5vcnRoZWFzdC0xIkcwRQIgEpAosy0seV2k2MBo2yi3yJOq%2FuhZuigX64JgZ7qycGQCIQCPoSN5OKyZgK9HnVwoHp9eXgbmMiC2%2FRqZT8%2BEsAK%2BxCqYBQgfEAAaDDM2OTA5NjQxOTE4NiIMBa%2FsDvUDy7FOlO70KvUElL3SCUgbbOWG7DuBynxF4WDd6YPVGamspM5SGeFe4ujTrrFnPIWl%2FjLJAKnEyw3hcj5snh3qD3Tz%2FMzRQSdaHXXcfRQzu1WaIP4h9JJfvohGgMilkR0mmiMUVyD0Du%2FR8WOYroZD6koiF8q9Ukm6%2BIDP4dGRE1OAnPzQw4%2FqJuq378RGPVYT6kE2loHXPJt0Yg627Oax2hbGtepJ4fF8HlivwXAkXlpKTzsf2T1mtulSlh2Io6WJcT%2FiYhnz6Dns77FgmtifHf6%2Fg5S6tvDlhz5sQDhwXN%2B%2FPML%2FVcNJPGdml7b2gn3Sk%2BehbxgT8zTey9Iy6A8fcWG0JVLDvrRqZi%2FwGyB1iMStpxFYJKh0w%2B%2F035dvv%2BbTNo0vahRysBXrl8sWoRFzHfiJvCWFRvdNuQKVC3OcTWpe8zZ18lM%2F6qPPG437HQeI4vXawUX2hK%2B8wOPEAmoHJWUb2uiSH7EVmCJebdTlbhA7GKPtV9ubROrDZGSO4Qbr7DkSMfPlACdAEItkUTT2QaJ5luGWL1C6ir2SGpu9asvjIzllsA9nNg9T0YXbbkbizPzh4kji0scbO2neke9IoHvr6OKuSnjoVkvO2tIrRGQ%2BTwvQsLrVHNpMzbqWk%2Bq8AAzJ%2F9oXpa2w2JDBylKwNfuPVEpyH7EtoHok1QX2ydC6iAJ7X4O8dmE5pgcF3meW8f2FqWktnWb8QjPoemGKl4yrREr9zN9eP1UGRbHHUBM990GL5NVWss%2F6hCPrSiXyimLS2aTNmt%2BfVzDMtHt6igiSeXdHWbm5UOojIE9KiIu1Iu0YUik4BNwrP%2FkfmC9kHMsFMBSFG7d8desTjGMwyKT8rAY6mwGT1na%2F0fJMDBYQYdef5p7DTAVtg91Js7k8QiXIZyqnJhr1uydYM0wEtzgqyeU7uNu0dKNPKtuiWghRvee6w4YkX7IvLxWzYQKAsvACJCc54TpjzSwnJ6mSHY0q5p67ibStZlQn7%2BaijGL5MQaW7lWabOUY0hZM8rH5Hb%2Fkp3vQV5jKSYdvmJaVoeUXtOfSNA6i7I2ek3AqnyYC1w%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240110T221332Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIAVL364M5ZNINEVMOX%2F20240110%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-Signature=3e230cf39dd8d55fec2ed2a6dd1382543d01ad611c4b120897992b1e84b16b99"
                },
                {
                    "reportType": "Transaction",
                    "transactionType": "Payout",
                    "transactionDate": "10/08/2023",
                    "fileName": "T_Payout_10082023.xlsx",
                    "downloadUrl": "https://tf-bin-prod-payment-merchant-admin.s3.ap-northeast-1.amazonaws.com/dailyReport/310903519/T_Payout_10082023.xlsx?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaDmFwLW5vcnRoZWFzdC0xIkcwRQIgEpAosy0seV2k2MBo2yi3yJOq%2FuhZuigX64JgZ7qycGQCIQCPoSN5OKyZgK9HnVwoHp9eXgbmMiC2%2FRqZT8%2BEsAK%2BxCqYBQgfEAAaDDM2OTA5NjQxOTE4NiIMBa%2FsDvUDy7FOlO70KvUElL3SCUgbbOWG7DuBynxF4WDd6YPVGamspM5SGeFe4ujTrrFnPIWl%2FjLJAKnEyw3hcj5snh3qD3Tz%2FMzRQSdaHXXcfRQzu1WaIP4h9JJfvohGgMilkR0mmiMUVyD0Du%2FR8WOYroZD6koiF8q9Ukm6%2BIDP4dGRE1OAnPzQw4%2FqJuq378RGPVYT6kE2loHXPJt0Yg627Oax2hbGtepJ4fF8HlivwXAkXlpKTzsf2T1mtulSlh2Io6WJcT%2FiYhnz6Dns77FgmtifHf6%2Fg5S6tvDlhz5sQDhwXN%2B%2FPML%2FVcNJPGdml7b2gn3Sk%2BehbxgT8zTey9Iy6A8fcWG0JVLDvrRqZi%2FwGyB1iMStpxFYJKh0w%2B%2F035dvv%2BbTNo0vahRysBXrl8sWoRFzHfiJvCWFRvdNuQKVC3OcTWpe8zZ18lM%2F6qPPG437HQeI4vXawUX2hK%2B8wOPEAmoHJWUb2uiSH7EVmCJebdTlbhA7GKPtV9ubROrDZGSO4Qbr7DkSMfPlACdAEItkUTT2QaJ5luGWL1C6ir2SGpu9asvjIzllsA9nNg9T0YXbbkbizPzh4kji0scbO2neke9IoHvr6OKuSnjoVkvO2tIrRGQ%2BTwvQsLrVHNpMzbqWk%2Bq8AAzJ%2F9oXpa2w2JDBylKwNfuPVEpyH7EtoHok1QX2ydC6iAJ7X4O8dmE5pgcF3meW8f2FqWktnWb8QjPoemGKl4yrREr9zN9eP1UGRbHHUBM990GL5NVWss%2F6hCPrSiXyimLS2aTNmt%2BfVzDMtHt6igiSeXdHWbm5UOojIE9KiIu1Iu0YUik4BNwrP%2FkfmC9kHMsFMBSFG7d8desTjGMwyKT8rAY6mwGT1na%2F0fJMDBYQYdef5p7DTAVtg91Js7k8QiXIZyqnJhr1uydYM0wEtzgqyeU7uNu0dKNPKtuiWghRvee6w4YkX7IvLxWzYQKAsvACJCc54TpjzSwnJ6mSHY0q5p67ibStZlQn7%2BaijGL5MQaW7lWabOUY0hZM8rH5Hb%2Fkp3vQV5jKSYdvmJaVoeUXtOfSNA6i7I2ek3AqnyYC1w%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240110T221332Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIAVL364M5ZNINEVMOX%2F20240110%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-Signature=a64c5c424bb2e3b046f4f48023b3cde86dd67af3007e812572d4d59ed272e7df"
                },
                {
                    "reportType": "Transaction",
                    "transactionType": "Payout",
                    "transactionDate": "09/08/2023",
                    "fileName": "T_Payout_09082023.xlsx",
                    "downloadUrl": "https://tf-bin-prod-payment-merchant-admin.s3.ap-northeast-1.amazonaws.com/dailyReport/310903519/T_Payout_09082023.xlsx?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaDmFwLW5vcnRoZWFzdC0xIkcwRQIgEpAosy0seV2k2MBo2yi3yJOq%2FuhZuigX64JgZ7qycGQCIQCPoSN5OKyZgK9HnVwoHp9eXgbmMiC2%2FRqZT8%2BEsAK%2BxCqYBQgfEAAaDDM2OTA5NjQxOTE4NiIMBa%2FsDvUDy7FOlO70KvUElL3SCUgbbOWG7DuBynxF4WDd6YPVGamspM5SGeFe4ujTrrFnPIWl%2FjLJAKnEyw3hcj5snh3qD3Tz%2FMzRQSdaHXXcfRQzu1WaIP4h9JJfvohGgMilkR0mmiMUVyD0Du%2FR8WOYroZD6koiF8q9Ukm6%2BIDP4dGRE1OAnPzQw4%2FqJuq378RGPVYT6kE2loHXPJt0Yg627Oax2hbGtepJ4fF8HlivwXAkXlpKTzsf2T1mtulSlh2Io6WJcT%2FiYhnz6Dns77FgmtifHf6%2Fg5S6tvDlhz5sQDhwXN%2B%2FPML%2FVcNJPGdml7b2gn3Sk%2BehbxgT8zTey9Iy6A8fcWG0JVLDvrRqZi%2FwGyB1iMStpxFYJKh0w%2B%2F035dvv%2BbTNo0vahRysBXrl8sWoRFzHfiJvCWFRvdNuQKVC3OcTWpe8zZ18lM%2F6qPPG437HQeI4vXawUX2hK%2B8wOPEAmoHJWUb2uiSH7EVmCJebdTlbhA7GKPtV9ubROrDZGSO4Qbr7DkSMfPlACdAEItkUTT2QaJ5luGWL1C6ir2SGpu9asvjIzllsA9nNg9T0YXbbkbizPzh4kji0scbO2neke9IoHvr6OKuSnjoVkvO2tIrRGQ%2BTwvQsLrVHNpMzbqWk%2Bq8AAzJ%2F9oXpa2w2JDBylKwNfuPVEpyH7EtoHok1QX2ydC6iAJ7X4O8dmE5pgcF3meW8f2FqWktnWb8QjPoemGKl4yrREr9zN9eP1UGRbHHUBM990GL5NVWss%2F6hCPrSiXyimLS2aTNmt%2BfVzDMtHt6igiSeXdHWbm5UOojIE9KiIu1Iu0YUik4BNwrP%2FkfmC9kHMsFMBSFG7d8desTjGMwyKT8rAY6mwGT1na%2F0fJMDBYQYdef5p7DTAVtg91Js7k8QiXIZyqnJhr1uydYM0wEtzgqyeU7uNu0dKNPKtuiWghRvee6w4YkX7IvLxWzYQKAsvACJCc54TpjzSwnJ6mSHY0q5p67ibStZlQn7%2BaijGL5MQaW7lWabOUY0hZM8rH5Hb%2Fkp3vQV5jKSYdvmJaVoeUXtOfSNA6i7I2ek3AqnyYC1w%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240110T221332Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIAVL364M5ZNINEVMOX%2F20240110%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-Signature=12dfe9fd26fd80f0462c4fe0b9e9b6485960a730a807b8cf273bf704aaad7890"
                },
                {
                    "reportType": "Transaction",
                    "transactionType": "Payout",
                    "transactionDate": "08/08/2023",
                    "fileName": "T_Payout_08082023.xlsx",
                    "downloadUrl": "https://tf-bin-prod-payment-merchant-admin.s3.ap-northeast-1.amazonaws.com/dailyReport/310903519/T_Payout_08082023.xlsx?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaDmFwLW5vcnRoZWFzdC0xIkcwRQIgEpAosy0seV2k2MBo2yi3yJOq%2FuhZuigX64JgZ7qycGQCIQCPoSN5OKyZgK9HnVwoHp9eXgbmMiC2%2FRqZT8%2BEsAK%2BxCqYBQgfEAAaDDM2OTA5NjQxOTE4NiIMBa%2FsDvUDy7FOlO70KvUElL3SCUgbbOWG7DuBynxF4WDd6YPVGamspM5SGeFe4ujTrrFnPIWl%2FjLJAKnEyw3hcj5snh3qD3Tz%2FMzRQSdaHXXcfRQzu1WaIP4h9JJfvohGgMilkR0mmiMUVyD0Du%2FR8WOYroZD6koiF8q9Ukm6%2BIDP4dGRE1OAnPzQw4%2FqJuq378RGPVYT6kE2loHXPJt0Yg627Oax2hbGtepJ4fF8HlivwXAkXlpKTzsf2T1mtulSlh2Io6WJcT%2FiYhnz6Dns77FgmtifHf6%2Fg5S6tvDlhz5sQDhwXN%2B%2FPML%2FVcNJPGdml7b2gn3Sk%2BehbxgT8zTey9Iy6A8fcWG0JVLDvrRqZi%2FwGyB1iMStpxFYJKh0w%2B%2F035dvv%2BbTNo0vahRysBXrl8sWoRFzHfiJvCWFRvdNuQKVC3OcTWpe8zZ18lM%2F6qPPG437HQeI4vXawUX2hK%2B8wOPEAmoHJWUb2uiSH7EVmCJebdTlbhA7GKPtV9ubROrDZGSO4Qbr7DkSMfPlACdAEItkUTT2QaJ5luGWL1C6ir2SGpu9asvjIzllsA9nNg9T0YXbbkbizPzh4kji0scbO2neke9IoHvr6OKuSnjoVkvO2tIrRGQ%2BTwvQsLrVHNpMzbqWk%2Bq8AAzJ%2F9oXpa2w2JDBylKwNfuPVEpyH7EtoHok1QX2ydC6iAJ7X4O8dmE5pgcF3meW8f2FqWktnWb8QjPoemGKl4yrREr9zN9eP1UGRbHHUBM990GL5NVWss%2F6hCPrSiXyimLS2aTNmt%2BfVzDMtHt6igiSeXdHWbm5UOojIE9KiIu1Iu0YUik4BNwrP%2FkfmC9kHMsFMBSFG7d8desTjGMwyKT8rAY6mwGT1na%2F0fJMDBYQYdef5p7DTAVtg91Js7k8QiXIZyqnJhr1uydYM0wEtzgqyeU7uNu0dKNPKtuiWghRvee6w4YkX7IvLxWzYQKAsvACJCc54TpjzSwnJ6mSHY0q5p67ibStZlQn7%2BaijGL5MQaW7lWabOUY0hZM8rH5Hb%2Fkp3vQV5jKSYdvmJaVoeUXtOfSNA6i7I2ek3AqnyYC1w%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240110T221332Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIAVL364M5ZNINEVMOX%2F20240110%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-Signature=973271dce83801930fac5b0730ed9007637d79f78fe280261d0cde21e6e6e9dc"
                },
                {
                    "reportType": "Transaction",
                    "transactionType": "Payout",
                    "transactionDate": "07/08/2023",
                    "fileName": "T_Payout_07082023.xlsx",
                    "downloadUrl": "https://tf-bin-prod-payment-merchant-admin.s3.ap-northeast-1.amazonaws.com/dailyReport/310903519/T_Payout_07082023.xlsx?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaDmFwLW5vcnRoZWFzdC0xIkcwRQIgEpAosy0seV2k2MBo2yi3yJOq%2FuhZuigX64JgZ7qycGQCIQCPoSN5OKyZgK9HnVwoHp9eXgbmMiC2%2FRqZT8%2BEsAK%2BxCqYBQgfEAAaDDM2OTA5NjQxOTE4NiIMBa%2FsDvUDy7FOlO70KvUElL3SCUgbbOWG7DuBynxF4WDd6YPVGamspM5SGeFe4ujTrrFnPIWl%2FjLJAKnEyw3hcj5snh3qD3Tz%2FMzRQSdaHXXcfRQzu1WaIP4h9JJfvohGgMilkR0mmiMUVyD0Du%2FR8WOYroZD6koiF8q9Ukm6%2BIDP4dGRE1OAnPzQw4%2FqJuq378RGPVYT6kE2loHXPJt0Yg627Oax2hbGtepJ4fF8HlivwXAkXlpKTzsf2T1mtulSlh2Io6WJcT%2FiYhnz6Dns77FgmtifHf6%2Fg5S6tvDlhz5sQDhwXN%2B%2FPML%2FVcNJPGdml7b2gn3Sk%2BehbxgT8zTey9Iy6A8fcWG0JVLDvrRqZi%2FwGyB1iMStpxFYJKh0w%2B%2F035dvv%2BbTNo0vahRysBXrl8sWoRFzHfiJvCWFRvdNuQKVC3OcTWpe8zZ18lM%2F6qPPG437HQeI4vXawUX2hK%2B8wOPEAmoHJWUb2uiSH7EVmCJebdTlbhA7GKPtV9ubROrDZGSO4Qbr7DkSMfPlACdAEItkUTT2QaJ5luGWL1C6ir2SGpu9asvjIzllsA9nNg9T0YXbbkbizPzh4kji0scbO2neke9IoHvr6OKuSnjoVkvO2tIrRGQ%2BTwvQsLrVHNpMzbqWk%2Bq8AAzJ%2F9oXpa2w2JDBylKwNfuPVEpyH7EtoHok1QX2ydC6iAJ7X4O8dmE5pgcF3meW8f2FqWktnWb8QjPoemGKl4yrREr9zN9eP1UGRbHHUBM990GL5NVWss%2F6hCPrSiXyimLS2aTNmt%2BfVzDMtHt6igiSeXdHWbm5UOojIE9KiIu1Iu0YUik4BNwrP%2FkfmC9kHMsFMBSFG7d8desTjGMwyKT8rAY6mwGT1na%2F0fJMDBYQYdef5p7DTAVtg91Js7k8QiXIZyqnJhr1uydYM0wEtzgqyeU7uNu0dKNPKtuiWghRvee6w4YkX7IvLxWzYQKAsvACJCc54TpjzSwnJ6mSHY0q5p67ibStZlQn7%2BaijGL5MQaW7lWabOUY0hZM8rH5Hb%2Fkp3vQV5jKSYdvmJaVoeUXtOfSNA6i7I2ek3AqnyYC1w%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240110T221332Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIAVL364M5ZNINEVMOX%2F20240110%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-Signature=bc0b2a7b6acb5875c7f6847e44f8a0903f9cc2b3bd53c399918c3a15ca329a6b"
                },
                {
                    "reportType": "Transaction",
                    "transactionType": "Payout",
                    "transactionDate": "05/08/2023",
                    "fileName": "T_Payout_05082023.xlsx",
                    "downloadUrl": "https://tf-bin-prod-payment-merchant-admin.s3.ap-northeast-1.amazonaws.com/dailyReport/310903519/T_Payout_05082023.xlsx?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaDmFwLW5vcnRoZWFzdC0xIkcwRQIgEpAosy0seV2k2MBo2yi3yJOq%2FuhZuigX64JgZ7qycGQCIQCPoSN5OKyZgK9HnVwoHp9eXgbmMiC2%2FRqZT8%2BEsAK%2BxCqYBQgfEAAaDDM2OTA5NjQxOTE4NiIMBa%2FsDvUDy7FOlO70KvUElL3SCUgbbOWG7DuBynxF4WDd6YPVGamspM5SGeFe4ujTrrFnPIWl%2FjLJAKnEyw3hcj5snh3qD3Tz%2FMzRQSdaHXXcfRQzu1WaIP4h9JJfvohGgMilkR0mmiMUVyD0Du%2FR8WOYroZD6koiF8q9Ukm6%2BIDP4dGRE1OAnPzQw4%2FqJuq378RGPVYT6kE2loHXPJt0Yg627Oax2hbGtepJ4fF8HlivwXAkXlpKTzsf2T1mtulSlh2Io6WJcT%2FiYhnz6Dns77FgmtifHf6%2Fg5S6tvDlhz5sQDhwXN%2B%2FPML%2FVcNJPGdml7b2gn3Sk%2BehbxgT8zTey9Iy6A8fcWG0JVLDvrRqZi%2FwGyB1iMStpxFYJKh0w%2B%2F035dvv%2BbTNo0vahRysBXrl8sWoRFzHfiJvCWFRvdNuQKVC3OcTWpe8zZ18lM%2F6qPPG437HQeI4vXawUX2hK%2B8wOPEAmoHJWUb2uiSH7EVmCJebdTlbhA7GKPtV9ubROrDZGSO4Qbr7DkSMfPlACdAEItkUTT2QaJ5luGWL1C6ir2SGpu9asvjIzllsA9nNg9T0YXbbkbizPzh4kji0scbO2neke9IoHvr6OKuSnjoVkvO2tIrRGQ%2BTwvQsLrVHNpMzbqWk%2Bq8AAzJ%2F9oXpa2w2JDBylKwNfuPVEpyH7EtoHok1QX2ydC6iAJ7X4O8dmE5pgcF3meW8f2FqWktnWb8QjPoemGKl4yrREr9zN9eP1UGRbHHUBM990GL5NVWss%2F6hCPrSiXyimLS2aTNmt%2BfVzDMtHt6igiSeXdHWbm5UOojIE9KiIu1Iu0YUik4BNwrP%2FkfmC9kHMsFMBSFG7d8desTjGMwyKT8rAY6mwGT1na%2F0fJMDBYQYdef5p7DTAVtg91Js7k8QiXIZyqnJhr1uydYM0wEtzgqyeU7uNu0dKNPKtuiWghRvee6w4YkX7IvLxWzYQKAsvACJCc54TpjzSwnJ6mSHY0q5p67ibStZlQn7%2BaijGL5MQaW7lWabOUY0hZM8rH5Hb%2Fkp3vQV5jKSYdvmJaVoeUXtOfSNA6i7I2ek3AqnyYC1w%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240110T221332Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIAVL364M5ZNINEVMOX%2F20240110%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-Signature=b909b1f48bed3dc805ded9c95e2168ce82206303af9cc755405ac30122fa54f8"
                },
                {
                    "reportType": "Transaction",
                    "transactionType": "Payout",
                    "transactionDate": "04/08/2023",
                    "fileName": "T_Payout_04082023.xlsx",
                    "downloadUrl": "https://tf-bin-prod-payment-merchant-admin.s3.ap-northeast-1.amazonaws.com/dailyReport/310903519/T_Payout_04082023.xlsx?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaDmFwLW5vcnRoZWFzdC0xIkcwRQIgEpAosy0seV2k2MBo2yi3yJOq%2FuhZuigX64JgZ7qycGQCIQCPoSN5OKyZgK9HnVwoHp9eXgbmMiC2%2FRqZT8%2BEsAK%2BxCqYBQgfEAAaDDM2OTA5NjQxOTE4NiIMBa%2FsDvUDy7FOlO70KvUElL3SCUgbbOWG7DuBynxF4WDd6YPVGamspM5SGeFe4ujTrrFnPIWl%2FjLJAKnEyw3hcj5snh3qD3Tz%2FMzRQSdaHXXcfRQzu1WaIP4h9JJfvohGgMilkR0mmiMUVyD0Du%2FR8WOYroZD6koiF8q9Ukm6%2BIDP4dGRE1OAnPzQw4%2FqJuq378RGPVYT6kE2loHXPJt0Yg627Oax2hbGtepJ4fF8HlivwXAkXlpKTzsf2T1mtulSlh2Io6WJcT%2FiYhnz6Dns77FgmtifHf6%2Fg5S6tvDlhz5sQDhwXN%2B%2FPML%2FVcNJPGdml7b2gn3Sk%2BehbxgT8zTey9Iy6A8fcWG0JVLDvrRqZi%2FwGyB1iMStpxFYJKh0w%2B%2F035dvv%2BbTNo0vahRysBXrl8sWoRFzHfiJvCWFRvdNuQKVC3OcTWpe8zZ18lM%2F6qPPG437HQeI4vXawUX2hK%2B8wOPEAmoHJWUb2uiSH7EVmCJebdTlbhA7GKPtV9ubROrDZGSO4Qbr7DkSMfPlACdAEItkUTT2QaJ5luGWL1C6ir2SGpu9asvjIzllsA9nNg9T0YXbbkbizPzh4kji0scbO2neke9IoHvr6OKuSnjoVkvO2tIrRGQ%2BTwvQsLrVHNpMzbqWk%2Bq8AAzJ%2F9oXpa2w2JDBylKwNfuPVEpyH7EtoHok1QX2ydC6iAJ7X4O8dmE5pgcF3meW8f2FqWktnWb8QjPoemGKl4yrREr9zN9eP1UGRbHHUBM990GL5NVWss%2F6hCPrSiXyimLS2aTNmt%2BfVzDMtHt6igiSeXdHWbm5UOojIE9KiIu1Iu0YUik4BNwrP%2FkfmC9kHMsFMBSFG7d8desTjGMwyKT8rAY6mwGT1na%2F0fJMDBYQYdef5p7DTAVtg91Js7k8QiXIZyqnJhr1uydYM0wEtzgqyeU7uNu0dKNPKtuiWghRvee6w4YkX7IvLxWzYQKAsvACJCc54TpjzSwnJ6mSHY0q5p67ibStZlQn7%2BaijGL5MQaW7lWabOUY0hZM8rH5Hb%2Fkp3vQV5jKSYdvmJaVoeUXtOfSNA6i7I2ek3AqnyYC1w%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240110T221332Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIAVL364M5ZNINEVMOX%2F20240110%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-Signature=234b61777dde9f6987301dc88ef7e91dcd3f157a9ce3fe56024195692f2df14a"
                },
                {
                    "reportType": "Transaction",
                    "transactionType": "Payout",
                    "transactionDate": "03/08/2023",
                    "fileName": "T_Payout_03082023.xlsx",
                    "downloadUrl": "https://tf-bin-prod-payment-merchant-admin.s3.ap-northeast-1.amazonaws.com/dailyReport/310903519/T_Payout_03082023.xlsx?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaDmFwLW5vcnRoZWFzdC0xIkcwRQIgEpAosy0seV2k2MBo2yi3yJOq%2FuhZuigX64JgZ7qycGQCIQCPoSN5OKyZgK9HnVwoHp9eXgbmMiC2%2FRqZT8%2BEsAK%2BxCqYBQgfEAAaDDM2OTA5NjQxOTE4NiIMBa%2FsDvUDy7FOlO70KvUElL3SCUgbbOWG7DuBynxF4WDd6YPVGamspM5SGeFe4ujTrrFnPIWl%2FjLJAKnEyw3hcj5snh3qD3Tz%2FMzRQSdaHXXcfRQzu1WaIP4h9JJfvohGgMilkR0mmiMUVyD0Du%2FR8WOYroZD6koiF8q9Ukm6%2BIDP4dGRE1OAnPzQw4%2FqJuq378RGPVYT6kE2loHXPJt0Yg627Oax2hbGtepJ4fF8HlivwXAkXlpKTzsf2T1mtulSlh2Io6WJcT%2FiYhnz6Dns77FgmtifHf6%2Fg5S6tvDlhz5sQDhwXN%2B%2FPML%2FVcNJPGdml7b2gn3Sk%2BehbxgT8zTey9Iy6A8fcWG0JVLDvrRqZi%2FwGyB1iMStpxFYJKh0w%2B%2F035dvv%2BbTNo0vahRysBXrl8sWoRFzHfiJvCWFRvdNuQKVC3OcTWpe8zZ18lM%2F6qPPG437HQeI4vXawUX2hK%2B8wOPEAmoHJWUb2uiSH7EVmCJebdTlbhA7GKPtV9ubROrDZGSO4Qbr7DkSMfPlACdAEItkUTT2QaJ5luGWL1C6ir2SGpu9asvjIzllsA9nNg9T0YXbbkbizPzh4kji0scbO2neke9IoHvr6OKuSnjoVkvO2tIrRGQ%2BTwvQsLrVHNpMzbqWk%2Bq8AAzJ%2F9oXpa2w2JDBylKwNfuPVEpyH7EtoHok1QX2ydC6iAJ7X4O8dmE5pgcF3meW8f2FqWktnWb8QjPoemGKl4yrREr9zN9eP1UGRbHHUBM990GL5NVWss%2F6hCPrSiXyimLS2aTNmt%2BfVzDMtHt6igiSeXdHWbm5UOojIE9KiIu1Iu0YUik4BNwrP%2FkfmC9kHMsFMBSFG7d8desTjGMwyKT8rAY6mwGT1na%2F0fJMDBYQYdef5p7DTAVtg91Js7k8QiXIZyqnJhr1uydYM0wEtzgqyeU7uNu0dKNPKtuiWghRvee6w4YkX7IvLxWzYQKAsvACJCc54TpjzSwnJ6mSHY0q5p67ibStZlQn7%2BaijGL5MQaW7lWabOUY0hZM8rH5Hb%2Fkp3vQV5jKSYdvmJaVoeUXtOfSNA6i7I2ek3AqnyYC1w%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240110T221332Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIAVL364M5ZNINEVMOX%2F20240110%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-Signature=f7f4931d19345d5ddcd9085527d1c1cd05b9aca46b56728d5f4d83b827f1b021"
                }
            ]
        }

    response = send_signed_request(
        'POST',
        '/binancepay/openapi/report/get-file',
        {
            "reportType": reportType,
            "transactionType": transactionType,
            "startDate": startDate,
            "endDate": endDate
        },
    )
    return response

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