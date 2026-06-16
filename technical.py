import pandas as pd

def calculate_indicators(df):

    df["MA5"] = df["收盘"].rolling(5).mean()

    df["MA10"] = df["收盘"].rolling(10).mean()

    df["MA20"] = df["收盘"].rolling(20).mean()

    return df
