# ======================================
# MULTI-CHART BUSINESS DASHBOARD
# ======================================

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load data
df = pd.read_csv("business_data.csv")

# --------------------------------------
# Create dashboard layout (2x2)
# --------------------------------------

fig = make_subplots(
    rows=2,
    cols=2,
    subplot_titles=("Sales", "Profit", "Expenses", "Customers")
)

# --------------------------------------
# Sales chart
# --------------------------------------

fig.add_trace(
    go.Scatter(x=df["month"], y=df["sales"], name="Sales"),
    row=1, col=1
)

# Profit chart
fig.add_trace(
    go.Bar(x=df["month"], y=df["profit"], name="Profit"),
    row=1, col=2
)

# Expenses chart
fig.add_trace(
    go.Scatter(x=df["month"], y=df["expenses"], name="Expenses"),
    row=2, col=1
)

# Customers chart
fig.add_trace(
    go.Scatter(x=df["month"], y=df["customers"], name="Customers"),
    row=2, col=2
)

fig.update_layout(title="Multi-Chart Business Dashboard")

fig.show()

"""
KEY IDEA:

This dashboard shows:
✔ multiple business metrics
✔ full overview in one screen
✔ easy comparison

Used in analytics platforms
"""