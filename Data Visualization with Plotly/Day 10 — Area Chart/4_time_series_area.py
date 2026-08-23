# ======================================
# TIME SERIES AREA VISUALIZATION
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("sales_trend.csv")
df["date"] = pd.to_datetime(df["date"])

# Sort data
df = df.sort_values("date")

# --------------------------------------
# Time-series area chart
# --------------------------------------

fig = px.area(
    df,
    x="date",
    y="sales",
    color="product",
    line_group="product",
    title="Time Series Area Visualization"
)

# Improve hover experience
fig.update_layout(
    hovermode="x unified"
)

fig.show()

"""
KEY IDEA:

Time series area chart shows:
✔ trends over time
✔ product contribution
✔ overall + breakdown view

This is very common in dashboards.
"""