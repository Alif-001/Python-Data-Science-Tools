# ======================================
# DAY 3: BASIC LINE PLOT
# ======================================

import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("sales_trend.csv")

# Convert date column to proper datetime format
df["date"] = pd.to_datetime(df["date"])

# --------------------------------------
# Basic line chart
# --------------------------------------
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Daily Sales Trend"
)

# Show interactive chart
fig.show()

"""
KEY IDEA:

px.line() is used to:
✔ Show trends over time
✔ Compare continuous data
✔ Detect patterns
"""