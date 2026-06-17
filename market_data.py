import akshare as ak

import pandas as pd

import time

def get_stock_data():

    for i in range(5):

        try:

            print(f"开始获取数据，第{i+1}次尝试")

            time.sleep(5)

            df = ak.stock_zh_a_spot_em()

            stock = df[df["代码"] == "600409"]

            if stock.empty:

                raise Exception("未找到股票")

            print("获取成功")

            stock.to_csv(

                "market_data.csv",

                index=False,

                encoding="utf-8-sig"

            )

            return stock

        except Exception as e:

            print(f"第{i+1}次失败")

            print(str(e))

            time.sleep(20)

    return None

df = get_stock_data()

if df is None:

    raise Exception("获取股票数据失败")
