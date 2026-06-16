import pandas as pd

def calculate_indicators(df):

    df["MA5"] = df["收盘"].rolling(5).mean()

    df["MA10"] = df["收盘"].rolling(10).mean()

    df["MA20"] = df["收盘"].rolling(20).mean()

    return df

def macd(df):

    ema12 = df["收盘"].ewm(span=12).mean()

    ema26 = df["收盘"].ewm(span=26).mean()

    df["DIF"] = ema12 - ema26

    df["DEA"] = df["DIF"].ewm(span=9).mean()

    df["MACD"] = (df["DIF"] - df["DEA"]) * 2

    return df
