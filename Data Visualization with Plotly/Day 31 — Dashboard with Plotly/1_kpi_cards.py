# ======================================
# DAY 31: KPI CARDS (KEY BUSINESS METRICS)
# ======================================

import pandas as pd
import plotly.graph_objects as go

# Load data
df = pd.read_csv("business_data.csv")

# --------------------------------------
# Calculate KPIs (important business metrics)
# --------------------------------------

total_sales = df["sales"].sum()
total_profit = df["profit"].sum()
total_expenses = df["expenses"].sum()
total_customers = df["customers"].sum()

# --------------------------------------
# Create KPI dashboard (simple layout)
# --------------------------------------

fig = go.Figure()

fig.add_trace(go.Indicator(
    mode="number",
    value=total_sales,
    title={"text": "Total Sales"},
    domain={"x": [0, 0.5], "y": [0.5, 1]}
))

fig.add_trace(go.Indicator(
    mode="number",
    value=total_profit,
    title={"text": "Total Profit"},
    domain={"x": [0.5, 1], "y": [0.5, 1]}
))

fig.add_trace(go.Indicator(
    mode="number",
    value=total_expenses,
    title={"text": "Total Expenses"},
    domain={"x": [0, 0.5], "y": [0, 0.5]}
))

fig.add_trace(go.Indicator(
    mode="number",
    value=total_customers,
    title={"text": "Total Customers"},
    domain={"x": [0.5, 1], "y": [0, 0.5]}
))

fig.update_layout(title="KPI Dashboard Cards")

fig.show()

"""
KEY IDEA:

KPI Cards show:
✔ total business performance
✔ executive summary
✔ quick insights

Used in CEO dashboards
"""