# ======================================
# MASTER BUSINESS DASHBOARD
# ======================================

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("master_data.csv")

# --------------------------------------
# KPI CALCULATIONS
# --------------------------------------

total_sales = df["sales"].sum()
total_profit = df["profit"].sum()
total_customers = df["customers"].sum()

# --------------------------------------
# CREATE DASHBOARD LAYOUT
# --------------------------------------

fig = make_subplots(
    rows=2,
    cols=2,
    subplot_titles=(
        "Sales Trend",
        "Profit Trend",
        "Ad Spend vs Sales",
        "Customers Trend"
    )
)

# Sales trend
fig.add_trace(
    go.Scatter(x=df["date"], y=df["sales"], mode="lines"),
    row=1, col=1
)

# Profit trend
fig.add_trace(
    go.Bar(x=df["date"], y=df["profit"]),
    row=1, col=2
)

# Ad spend vs sales
fig.add_trace(
    go.Scatter(x=df["ad_spend"], y=df["sales"], mode="markers"),
    row=2, col=1
)

# Customers trend
fig.add_trace(
    go.Scatter(x=df["date"], y=df["customers"], mode="lines"),
    row=2, col=2
)

fig.update_layout(
    title="📊 Master Business Dashboard",
    showlegend=False,
    height=700
)

fig.show()

"""
KEY IDEA:

✔ real business dashboard structure
✔ multiple insights in one view
"""