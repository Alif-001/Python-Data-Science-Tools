# ======================================
# ADVANCED SUBPLOTS DASHBOARD
# ======================================

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("sales_data.csv")

# --------------------------------------
# Advanced 2x2 dashboard
# --------------------------------------

fig = make_subplots(
    rows=2,
    cols=2,
    subplot_titles=("Sales", "Profit", "Expenses", "Profit Trend")
)

# Sales line chart
fig.add_trace(
    go.Scatter(x=df["month"], y=df["sales"], name="Sales"),
    row=1, col=1
)

# Profit bar chart
fig.add_trace(
    go.Bar(x=df["month"], y=df["profit"], name="Profit"),
    row=1, col=2
)

# Expenses line chart
fig.add_trace(
    go.Scatter(x=df["month"], y=df["expenses"], name="Expenses"),
    row=2, col=1
)

# Profit trend line
fig.add_trace(
    go.Scatter(x=df["month"], y=df["profit"], name="Profit Trend"),
    row=2, col=2
)

# --------------------------------------
# Layout styling (dashboard look)
# --------------------------------------

fig.update_layout(
    title="Advanced Business Dashboard",
    showlegend=False
)

fig.show()

"""
KEY IDEA:

Advanced subplots give:
✔ professional dashboards
✔ KPI monitoring
✔ multi-metric comparison
"""