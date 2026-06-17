import akshare as ak

import pandas as pd

try:

    df = ak.stock_zh_a_hist(

        symbol="600409",

        period="daily",

        adjust=""

    )

    if df.empty:

        raise Exception("未获取到数据")

    latest = df.iloc[-1]

    result = pd.DataFrame([

        {

            "代码": "600409",

            "名称": "三友化工",

            "日期": latest["日期"],

            "开盘": latest["开盘"],

            "最高": latest["最高"],

            "最低": latest["最低"],

            "收盘": latest["收盘"],

            "成交量": latest["成交量"],

            "成交额": latest["成交额"]

        }

    ])

    result.to_csv(

        "market_data.csv",

        index=False,

        encoding="utf-8-sig"

    )

    print(result)

    print("market_data.csv 已保存")

except Exception as e:

    print(e)

    raise
