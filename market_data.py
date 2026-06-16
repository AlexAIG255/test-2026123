import akshare as ak

import time

def get_stock_data():

    for i in range(5):

        try:

            df = ak.stock_zh_a_hist(

                symbol="600409",

                period="daily",

                start_date="20240101",

                end_date="20260616",

                adjust=""

            )

            return df

        except Exception as e:

            print(f"第{i+1}次失败")

            print(e)

            time.sleep(10)

    return None

df = get_stock_data()

if df is not None:

    print(df.tail())

else:

    print("最终失败")
