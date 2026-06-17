import os
import requests

webhook = os.getenv(“WECOM_WEBHOOK”)

if not webhook:
raise Exception(“WECOM_WEBHOOK 未配置”)

with open(
“analysis_result.txt”,
“r”,
encoding=“utf-8”
) as f:
content = f.read()

payload = {
“msgtype”: “text”,
“text”: {
“content”: content
}
}

r = requests.post(
webhook,
json=payload,
timeout=20
)

print(r.text)
