import os

import requests

import pandas as pd

webhook = os.getenv("WECOM_WEBHOOK")

if not webhook:

    raise Exception("WECOM_WEBHOOK not configured")

df = pd.read_csv("market_data.csv")

latest = df.iloc[-1]

price = float(latest["最新价"])

change = float(latest["涨跌幅"])

alert = None

if change >= 5:

    alert = f"UP ALERT: price={price}, change={change}%"

elif change <= -5:

    alert = f"DOWN ALERT: price={price}, change={change}%"

if alert:

    payload = {

        "msgtype": "text",

        "text": {"content": alert}

    }

    r = requests.post(webhook, json=payload, timeout=20)

    print(r.text)

else:

    print("NO ALERT")
