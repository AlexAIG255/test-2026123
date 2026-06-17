import pandas as pd

try:

df = pd.read_csv("market_data.csv")

latest = df.iloc[-1]

report = f"""

股票: {latest['名称']}代码: {latest['代码']}最新价: {latest['最新价']}涨跌幅: {latest['涨跌幅']}%"""

print(report)

with open(
    "daily_report.md",
    "w",
    encoding="utf-8"
) as f:
    f.write(report)

except Exception as e:

print("Monitor Error:", e)

raise
