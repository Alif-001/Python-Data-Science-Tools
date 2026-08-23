# ======================================
# DAY 28: MULTIPLE TRACES
# ======================================

import pandas as pd
import plotly.graph_objects as go

# Load dataset
df = pd.read_csv("sales_finance.csv")

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
# Trace 3: Marketing Cost
# --------------------------------------

fig.add_trace(
    go.Scatter(
        x=df["month"],
        y=df["marketing_cost"],
        mode="lines+markers",
        name="Marketing Cost"
    )
)

# --------------------------------------
# Layout
# --------------------------------------

fig.update_layout(
    title="Multiple Traces Dashboard",
    xaxis_title="Month",
    yaxis_title="Value"
)

fig.show()

"""
KEY IDEA:

Multiple traces = multiple datasets in one chart
✔ compare business metrics
✔ build dashboards
✔ analyze trends together
"""