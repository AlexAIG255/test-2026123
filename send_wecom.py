import os

import requests

webhook = os.getenv("WECOM_WEBHOOK")

if not webhook:

    raise Exception("WECOM_WEBHOOK not found")

msg = {

    "msgtype": "text",

    "text": {

        "content": "AI Stock Agent 测试成功"

    }

}

requests.post(webhook, json=msg)
