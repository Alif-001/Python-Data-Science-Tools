# ======================================
# FULL BUSINESS DASHBOARD (PRO LEVEL)
# ======================================

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("business_data.csv")

# --------------------------------------
# Create advanced dashboard layout
# --------------------------------------

fig = make_subplots(
    rows=2,
    cols=2,
    subplot_titles=(
        "Sales Trend",
        "Profit Trend",
        "Expenses Trend",
        "Customer Growth"
    )
)

# --------------------------------------
# Sales (line + markers)
# --------------------------------------

fig.add_trace(
    go.Scatter(
        x=df["month"],
        y=df["sales"],
        mode="lines+markers",
        name="Sales"
    ),
    row=1, col=1
)

# Profit
fig.add_trace(
    go.Scatter(
        x=df["month"],
        y=df["profit"],
        mode="lines+markers",
        name="Profit"
    ),
    row=1, col=2
)

# Expenses
fig.add_trace(
    go.Bar(
        x=df["month"],
        y=df["expenses"],
        name="Expenses"
    ),
    row=2, col=1
)

# Customers
fig.add_trace(
    go.Scatter(
        x=df["month"],
        y=df["customers"],
        mode="lines+markers",
        name="Customers"
    ),
    row=2, col=2
)

# --------------------------------------
# Dashboard styling
# --------------------------------------

fig.update_layout(
    title="📊 Executive Business Dashboard",
    showlegend=False,
    height=700
)

fig.show()

"""
KEY IDEA:

This is REAL dashboard design:

✔ KPI overview
✔ multiple charts
✔ executive reporting view

Used in real companies
"""