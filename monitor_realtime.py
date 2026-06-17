import os
import requests
import pandas as pd

webhook = os.getenv(“WECOM_WEBHOOK”)

if not webhook:
raise Exception(“WECOM_WEBHOOK 未配置”)

df = pd.read_csv(“market_data.csv”)

latest = df.iloc[-1]

price = float(latest[“最新价”])

change = float(latest[“涨跌幅”])

alert = None

if change >= 5:
alert = f”””
三友化工上涨预警

当前价格：{price}

涨跌幅：{change}%
“””

elif change <= -5:
alert = f”””
三友化工下跌预警

当前价格：{price}

涨跌幅：{change}%
“””

if alert:
