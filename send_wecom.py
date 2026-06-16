import os

import requests

webhook = os.getenv("WECOM_WEBHOOK")

content = """

【三友化工】

当前价格：6.53

MA5：6.42

MA10：6.31

MACD：金叉

AI评分：82

建议：买入

"""

msg = {

    "msgtype": "text",

    "text": {

        "content": content

    }

}

requests.post(webhook, json=msg)
