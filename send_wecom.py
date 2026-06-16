import os

import requests

webhook = os.getenv("WECOM_WEBHOOK")

msg = {

    "msgtype": "text",

    "text": {

        "content": "AI Stock Agent 测试成功"

    }

}

requests.post(webhook, json=msg)
