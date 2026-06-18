import os

import pandas as pd

from google import genai

api_key = os.getenv("GEMINI_API_KEY")

print("KEY:", "OK" if api_key else "EMPTY")

if not api_key:

    raise Exception("GEMINI_API_KEY missing")

client = genai.Client(api_key=api_key)

df = pd.read_csv("market_data.csv")

latest = df.iloc[-1]

prompt = f"""

股票代码: {latest['代码']}

名称: {latest['名称']}

最新价: {latest['最新价']}

涨跌幅: {latest['涨跌幅']}

分析主力行为并给出交易建议

"""

response = client.models.generate_content(

    model="gemini-2.5-flash",

    contents=prompt

)

with open("analysis_result.txt", "w", encoding="utf-8") as f:

    f.write(response.text)

print(response.text)
