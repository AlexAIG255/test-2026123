import os

import pandas as pd

import google.generativeai as genai

api_key = os.getenv("GEMINI_API_KEY")

print("Gemini Key:", "OK" if api_key else "EMPTY")

if not api_key:

    raise Exception("GEMINI_API_KEY Secret Missing")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

df = pd.read_csv("market_data.csv")

latest = df.iloc[-1]

prompt = f"""

你是一名职业A股操盘手。

股票代码：{latest['代码']}

股票名称：{latest['名称']}

最新价：{latest['最新价']}

涨跌幅：{latest['涨跌幅']}%

请分析：

1. 主力意图

2. 是否洗盘

3. 是否出货

4. 明日走势预测

5. 买入区间

6. 止损位

7. 目标位

最后给出：

买入

观望

卖出

三选一

"""

response = model.generate_content(prompt)

with open(

    "analysis_result.txt",

    "w",

    encoding="utf-8"

) as f:

    f.write(response.text)

print(response.text)
