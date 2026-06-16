from market_data import get_stock_data

from technical import calculate_indicators

from technical import macd

from signal import generate_signal

code = "600409"

df = get_stock_data(code)

df = calculate_indicators(df)

df = macd(df)

signal, score = generate_signal(df)

print("股票:", code)

print("信号:", signal)

print("评分:", score)
