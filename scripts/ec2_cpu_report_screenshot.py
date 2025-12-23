# scripts/ec2_cpu_report_screenshot.py

import os
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table

# ------------------------
# Example data
# Replace this with dynamic EC2 metrics later
# ------------------------
data = [
    {
        "instance_id": "i-1234567890abcdef0",
        "instance_type": "t2.micro",
        "state": "running",
        "launch_time": "1/15/2024",
        "avg_cpu_percent": 3.5,
        "recommendation": "Consider stopping - low utilization",
        "estimated_monthly_cost": 8.5,
    }
]

df = pd.DataFrame(data)

# ------------------------
# Ensure screenshots folder exists
# ------------------------
screenshots_folder = "screenshots"
os.makedirs(screenshots_folder, exist_ok=True)

# ------------------------
# Create figure and table
# ------------------------
fig, ax = plt.subplots(figsize=(10, 2))
ax.axis("tight")
ax.axis("off")

tbl = table(ax, df, loc="center", cellLoc="center")
tbl.auto_set_font_size(False)
tbl.set_fontsize(10)
tbl.scale(1.2, 1.2)

# ------------------------
# Save screenshot
# ------------------------
output_path = os.path.join(screenshots_folder, "ec2_cpu_report.png")
plt.savefig(output_path, bbox_inches="tight")
print(f"[INFO] Screenshot saved to {output_path}")

plt.close()
