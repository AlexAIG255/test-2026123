import requests

import pandas as pd

url="https://qt.gtimg.cn/q=sh600409"

r=requests.get(

    url,

    headers={

        "User-Agent":"Mozilla/5.0"

    },

    timeout=10

)

txt=r.text

print(txt)
