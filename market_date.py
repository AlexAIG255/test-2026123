import akshare as ak

stock = ak.stock_zh_a_hist(

    symbol="600409",

    period="daily",

    adjust=""

)

print(stock.tail())
