import os
import pandas as pd
import google.generativeai as genai

api_key = os.getenv(“GEMINI_API_KEY”)

if not api_key:
raise Exception(“GEMINI_API_KEY 未配置”)

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
“gemini-2.5-flash”
)

df = pd.read_csv(“market_data.csv”)

latest = df.iloc[-1]

prompt = f”””
你是一名职业A股操盘手。

股票代码：
{latest[‘代码’]}

股票名称：
{latest[‘名称’]}

最新价：
{latest[‘最新价’]}

涨跌幅：
{latest[‘涨跌幅’]}%

请分析：

1. 主力意图
2. 是否洗盘
3. 是否出货
4. 支撑位
5. 压力位
6. 明日走势预测
7. 操作建议

最后只给出：

买入
观望
卖出

三选一。
“””

response = model.generate_content(prompt)

with open(
“analysis_result.txt”,
“w”,
encoding=“utf-8”
) as f:
f.write(response.text)

print(response.text)
