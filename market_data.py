import akshare as ak

import pandas as pd

def get_stock_data(code):

    df = ak.stock_zh_a_hist(

        symbol=code,

        period="daily",

        adjust="qfq"

    )

    return df.tail(60)

if __name__ == "__main__":

    df = get_stock_data("600409")

    print(df.tail())
