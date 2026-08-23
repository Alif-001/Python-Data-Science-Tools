# ======================================
# CUMULATIVE TREND
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_trend.csv")
df["date"] = pd.to_datetime(df["date"])

# --------------------------------------
# Create total sales per day
# --------------------------------------
daily = df.groupby("date")["sales"].sum().reset_index()

# --------------------------------------
# Area chart for cumulative trend
# --------------------------------------

fig = px.area(
    daily,
    x="date",
    y="sales",
    title="Cumulative Sales Trend"
)

fig.show()

"""
KEY IDEA:

Cumulative trend shows:
✔ overall growth
✔ business performance over time
✔ total market movement
"""