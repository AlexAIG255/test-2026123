import os
import requests
import pandas as pd

webhook = os.getenv(“WECOM_WEBHOOK”)

if not webhook:
raise Exception(“WECOM_WEBHOOK not configured”)

df = pd.read_csv(“market_data.csv”)

latest = df.iloc[-1]

price = float(latest[“最新价”])
change = float(latest[“涨跌幅”])

alert = None

if change >= 5:
alert = f”””
Stock Alert

Symbol: 600409
Price: {price}
Change: {change}%

Strong Up Move Detected
“””

elif change <= -5:
alert = f”””
Stock Alert

Symbol: 600409
Price: {price}
Change: {change}%

Strong Down Move Detected
“””

if alert:
