import akshare as ak

import pandas as pd

try:

    df = ak.stock_individual_fund_flow(stock="600409")

    print(df.tail())

except Exception as e:

    print("Fund Flow Error:", e)

    pd.DataFrame({

        "error": [str(e)]

    }).to_csv("fund_flow.csv", index=False)
