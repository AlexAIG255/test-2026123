import os

import tushare as ts

import pandas as pd

token = os.getenv("TUSHARE_TOKEN")

if not token:

    raise Exception("TUSHARE_TOKEN 未配置")

ts.set_token(token)

pro = ts.pro_api()

df = pro.daily(

    ts_code="600409.SH"

)

if df.empty:

    raise Exception("未获取到数据")

latest = df.iloc[0]

result = pd.DataFrame([

    {

        "代码": "600409",

        "名称": "三友化工",

        "最新价": latest["close"],

        "涨跌幅": latest["pct_chg"],

        "成交量": latest["vol"]

    }

])

result.to_csv(

    "market_data.csv",

    index=False,

    encoding="utf-8-sig"

)

print(result)

print("market_data.csv 已保存")
