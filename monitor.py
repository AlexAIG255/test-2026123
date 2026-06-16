from analysis import analyze

import requests

import os

report=analyze()

print(report)

with open(

    "reports/daily_report.md",

    "w",

    encoding="utf-8"

) as f:

    f.write(report)
