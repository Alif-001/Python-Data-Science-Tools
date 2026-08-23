# ======================================
# DAY 10: BASIC AREA CHART
# ======================================

import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("sales_trend.csv")

# Convert date to proper format
df["date"] = pd.to_datetime(df["date"])

# Sort by date (IMPORTANT)
df = df.sort_values("date")

# --------------------------------------
# Basic area chart
# --------------------------------------

fig = px.area(
    df,
    x="date",
    y="sales",
    title="Basic Area Chart (Total Sales)"
)

fig.show()

"""
KEY IDEA:

Area chart = line chart + filled area below it

Used for:
✔ showing growth
✔ cumulative trends
✔ magnitude over time
"""