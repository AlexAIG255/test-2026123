import requests

def get_fund_flow():

    url="https://push2.eastmoney.com/api/qt/clist/get"

    params={

        "pn":"1",

        "pz":"20",

        "fid":"f62"

    }

    r=requests.get(url,params=params)

    return r.text

print(get_fund_flow())
