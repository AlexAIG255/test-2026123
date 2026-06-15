import os

import requests

webhook = os.environ["WECOM_WEBHOOK"]

with open(

    "reports/daily_report.md",

    "r",

    encoding="utf-8"

) as f:

    report = f.read()

payload = {

    "msgtype": "text",

    "text": {

        "content": report[:4000]

    }

}

response = requests.post(

    webhook,

    json=payload,

    timeout=30

)

print(response.text)
