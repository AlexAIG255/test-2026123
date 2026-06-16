import requests

code="sh600409"

url=f"https://qt.gtimg.cn/q={code}"

r=requests.get(url)

print(r.text)
