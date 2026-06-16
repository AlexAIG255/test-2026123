import akshare as ak

symbol = "600409"

df = ak.stock_zh_a_spot_em()

stock = df[df["代码"] == symbol]

price = float(stock.iloc[0]["最新价"])

change = float(stock.iloc[0]["涨跌幅"])

print(price)

print(change)

if change >= 5:

    print("暴涨预警")

if change <= -5:

    print("暴跌预警")
  import os

import requests

import akshare as ak

webhook = os.getenv("WECOM_WEBHOOK")

symbol = "600409"

df = ak.stock_zh_a_spot_em()

stock = df[df["代码"] == symbol]

price = float(stock.iloc[0]["最新价"])

change = float(stock.iloc[0]["涨跌幅"])

if change >= 5:

    msg = {

        "msgtype": "text",

        "text": {

            "content":

            f"""

三友化工异动提醒

当前价格:{price}

涨幅:{change}%

            """

        }

    }

    requests.post(webhook, json=msg)
