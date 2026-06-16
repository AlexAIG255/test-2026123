def generate_signal(df):

    last = df.iloc[-1]

    score = 50

    if last["MA5"] > last["MA10"]:

        score += 20

    if last["MACD"] > 0:

        score += 20

    if score >= 70:

        signal = "买入"

    elif score <= 30:

        signal = "卖出"

    else:

        signal = "观望"

    return signal, score
