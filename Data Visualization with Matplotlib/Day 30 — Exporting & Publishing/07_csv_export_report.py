import pandas as pd
import matplotlib.pyplot as plt

"""
CSV REPORT + EXPORT
-------------------
Real-world workflow:
1. Load data
2. Plot
3. Export as report image
"""

df = pd.read_csv("report_data.csv")

plt.figure(figsize=(10, 6))

plt.plot(df["day"], df["sales"], label="Sales")
plt.plot(df["day"], df["profit"], label="Profit")

plt.title("Business Report Chart")
plt.xlabel("Day")
plt.ylabel("Value")

plt.legend()
plt.grid(True)

# Save report image
plt.savefig("business_report.png", dpi=300, bbox_inches="tight")

plt.show()