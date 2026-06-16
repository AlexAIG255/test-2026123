import os

webhook = os.getenv("WECOM_WEBHOOK")

print("Webhook =", webhook)

if webhook is None:

    raise Exception("Secret Empty")
