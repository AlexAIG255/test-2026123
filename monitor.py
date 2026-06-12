from pathlib import Path

from datetime import datetime

print("=" * 50)

print("AI Trading Agent")

print("=" * 50)

print("\nLoading Skills...")

skills_path = Path("skills")

for file in skills_path.glob("*.md"):

    print(f"\n[{file.name}]")

    content = file.read_text(

        encoding="utf-8"

    )

    print(content[:200])

print("\nLoading Knowledge...")

knowledge_path = Path("knowledge")

for file in knowledge_path.glob("*.md"):

    print(f"\n[{file.name}]")

    content = file.read_text(

        encoding="utf-8"

    )

    print(content[:200])

print("\nGenerating Report...")

report = f"""

# Daily Report

Date:

{datetime.now()}

Status:

Agent Running Normal

"""

Path(

    "reports/daily_report.md"

).write_text(

    report,

    encoding="utf-8"

)

print("Report Saved")

print("\nDone")
