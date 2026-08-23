# ======================================
# DASHBOARD STYLE SUBPLOTS
# ======================================

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("sales_data.csv")

# --------------------------------------
# Create dashboard layout (2x2 grid)
# --------------------------------------

fig = make_subplots(
    rows=2,
    cols=2,
    subplot_titles=("Sales", "Profit", "Expenses", "Sales Trend")
)

# --------------------------------------
# Top-left: Sales
# --------------------------------------

fig.add_trace(
    go.Scatter(x=df["month"], y=df["sales"], name="Sales"),
    row=1, col=1
)

# Top-right: Profit
fig.add_trace(
    go.Bar(x=df["month"], y=df["profit"], name="Profit"),
    row=1, col=2
)

# Bottom-left: Expenses
fig.add_trace(
    go.Scatter(x=df["month"], y=df["expenses"], name="Expenses"),
    row=2, col=1
)

# Bottom-right: Sales trend again
fig.add_trace(
    go.Scatter(x=df["month"], y=df["sales"], name="Trend"),
    row=2, col=2
)

fig.update_layout(title="Dashboard Layout Example")

fig.show()

"""
KEY IDEA:

This creates:
✔ full dashboard view
✔ multiple metrics at once
✔ business-style analytics screen
"""