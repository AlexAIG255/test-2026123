import requests

url = "https://hq.sinajs.cn/list=sh600409"

headers = {

    "Referer": "https://finance.sina.com.cn"

}

r = requests.get(url, headers=headers)

print(r.text)
