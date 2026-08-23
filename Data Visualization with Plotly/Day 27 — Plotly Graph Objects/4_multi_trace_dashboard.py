# ======================================
# MULTI-TRACE DASHBOARD (ADVANCED)
# ======================================

import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("sales_data.csv")

# --------------------------------------
# Create figure
# --------------------------------------

fig = go.Figure()

# --------------------------------------
# Trace 1: Sales
# --------------------------------------

fig.add_trace(
    go.Scatter(
        x=df["month"],
        y=df["sales"],
        mode="lines+markers",
        name="Sales"
    )
)

# --------------------------------------
# Trace 2: Profit
# --------------------------------------

fig.add_trace(
    go.Scatter(
        x=df["month"],
        y=df["profit"],
        mode="lines+markers",
        name="Profit"
    )
)

# --------------------------------------
# Trace 3: Expenses
# --------------------------------------

fig.add_trace(
    go.Scatter(
        x=df["month"],
        y=df["expenses"],
        mode="lines+markers",
        name="Expenses"
    )
)

# --------------------------------------
# Final layout
# --------------------------------------

fig.update_layout(
    title="Business Performance Dashboard",
    xaxis_title="Month",
    yaxis_title="Value",
    legend_title="Metrics"
)

fig.show()

"""
KEY IDEA:

Multi-trace figure:
✔ multiple datasets in one chart
✔ dashboard-style visualization
✔ full control over everything
"""