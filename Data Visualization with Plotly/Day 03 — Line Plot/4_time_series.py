# ======================================
# TIME SERIES VISUALIZATION
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_trend.csv")

# Convert to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date (VERY IMPORTANT)
df = df.sort_values("date")

# --------------------------------------
# Time series line chart
# --------------------------------------
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Time Series Sales Analysis"
)

# --------------------------------------
# Layout improvement
# --------------------------------------
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales",
    hovermode="x unified"  # shows all values on hover
)

fig.show()

"""
KEY IDEA:

Time series = ordered data over time

IMPORTANT RULES:
✔ Always sort by date
✔ Convert string → datetime
✔ Use hovermode for better UX
"""