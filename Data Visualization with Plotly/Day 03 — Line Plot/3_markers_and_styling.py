# ======================================
# MARKERS + LINE STYLING
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_trend.csv")
df["date"] = pd.to_datetime(df["date"])

# --------------------------------------
# Line with markers
# --------------------------------------
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Sales Trend with Markers"
)

# Add markers (important for data points visibility)
fig.update_traces(
    mode="lines+markers",  # line + dots
    line=dict(color="blue", width=3)
)

fig.show()

"""
KEY IDEAS:

mode:
- lines → only line
- markers → only dots
- lines+markers → both

Styling helps:
✔ readability
✔ presentation quality
"""