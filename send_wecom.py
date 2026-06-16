import os

import requests

webhook = os.getenv("WECOM_WEBHOOK")

print("Webhook =", webhook)

msg = {

    "msgtype": "text",

    "text": {

        "content": "AI Stock Agent 测试消息"

    }

}

r = requests.post(webhook, json=msg)

print("Status Code:", r.status_code)

print("Response:", r.text)
