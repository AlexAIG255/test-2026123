import pandas as pd

try:

    df = pd.read_csv("market_data.csv")

    latest = df.iloc[-1]

    name = str(latest["名称"])

    code = str(latest["代码"])

    price = float(latest["最新价"])

    change = float(latest["涨跌幅"])

    report = f"""

Stock: {name}

Code: {code}

Price: {price}

Change: {change}%

"""

    if change >= 5:

        report += "\nALERT: STRONG UP MOVE\n"

    elif change <= -5:

        report += "\nALERT: STRONG DOWN MOVE\n"

    else:

        report += "\nStatus: NORMAL\n"

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
