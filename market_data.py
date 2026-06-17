import requests
import pandas as pd

url = "https://qt.gtimg.cn/q=sh600409"

r = requests.get(
url,
headers={
"User-Agent": "Mozilla/5.0"
},
timeout=10
)

text = r.text

print(text)

parts = text.split("~")

if len(parts) < 40:
raise Exception("腾讯行情接口返回异常")

result = pd.DataFrame([
{
"代码": "600409",
"名称": parts[1],
"最新价": float(parts[3]),
"昨收": float(parts[4]),
"开盘": float(parts[5]),
"成交量": parts[36]
}
])

result["涨跌幅"] = (
(result["最新价"] - result["昨收"])
/ result["昨收"]
* 100
).round(2)

result.to_csv(
“market_data.csv”,
index=False,
encoding=“utf-8-sig"
)

print(result)
