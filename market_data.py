import akshare as ak

import pandas as pd

try:

    df = ak.stock_zh_a_spot_em()

    stock = df[df["代码"] == "600409"]

    stock.to_csv(

        "market_data.csv",

        index=False,

        encoding="utf-8-sig"

    )

    print(stock)

except Exception as e:

    print(e)

    pd.DataFrame(

        [{

            "代码":"600409",

            "名称":"三友化工",

            "最新价":0,

            "涨跌幅":0

        }]

    ).to_csv(

        "market_data.csv",

        index=False,

        encoding="utf-8-sig"

    )

    print("使用备用数据")
