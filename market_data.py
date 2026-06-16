import requests

def get_stock(code):

    if code.startswith("6"):

        symbol=f"sh{code}"

    else:

        symbol=f"sz{code}"

    url=f"https://qt.gtimg.cn/q={symbol}"

    text=requests.get(url).text

    return text

print(get_stock("600409"))
