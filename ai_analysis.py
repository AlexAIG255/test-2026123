import os
import pandas as pd
from google import genai

api_key = os.getenv(“GEMINI_API_KEY”)

if not api_key:
raise Exception(“GEMINI_API_KEY missing”)

client = genai.Client(api_key=api_key)

df = pd.read_csv(“market_data.csv”)
latest = df.iloc[-1]

prompt = f”””
你是一名A股交易分析师。

股票代码: {latest[‘代码’]}
名称: {latest[‘名称’]}
最新价: {latest[‘最新价’]}
涨跌幅: {latest[‘涨跌幅’]}%

请分析并给出：

1. 主力意图
2. 趋势判断
3. 买卖建议
    “””

response = client.models.generate_content(
model=“gemini-2.5-flash”,
contents=prompt
)

with open(“analysis_result.txt”, “w”, encoding=“utf-8”) as f:
f.write(response.text)

print(response.text)
