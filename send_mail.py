import os

import smtplib

from email.mime.text import MIMEText

sender = os.environ["EMAIL_USER"]

password = os.environ["EMAIL_PASS"]

receiver = os.environ["EMAIL_TO"]

with open("reports/daily_report.md","r",encoding="utf-8") as f:

    report = f.read()

msg = MIMEText(report,"plain","utf-8")

msg["Subject"] = "AI股票日报"

msg["From"] = sender

msg["To"] = receiver

server = smtplib.SMTP_SSL(

    "smtp.qq.com",

    465

)

server.login(

    sender,

    password

)

server.sendmail(

    sender,

    receiver,

    msg.as_string()

)

server.quit()

print("Email Sent")
