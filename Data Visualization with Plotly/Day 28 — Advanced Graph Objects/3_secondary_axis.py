# ======================================
# SECONDARY Y-AXIS (VERY IMPORTANT)
# ======================================

import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("sales_finance.csv")

# --------------------------------------
# Create figure
# --------------------------------------

fig = go.Figure()

# --------------------------------------
# Sales (Primary axis)
# --------------------------------------

fig.add_trace(go.Scatter(
    x=df["month"],
    y=df["sales"],
    name="Sales",
    yaxis="y1"
))

# --------------------------------------
# Marketing Cost (Secondary axis)
# --------------------------------------

fig.add_trace(go.Scatter(
    x=df["month"],
    y=df["marketing_cost"],
    name="Marketing Cost",
    yaxis="y2"
))

# --------------------------------------
# Layout with dual axis
# --------------------------------------

fig.update_layout(
    title="Secondary Axis Example",

    xaxis=dict(title="Month"),

    yaxis=dict(
        title="Sales",
        side="left"
    ),

    yaxis2=dict(
        title="Marketing Cost",
        overlaying="y",
        side="right"
    )
)

fig.show()

"""
KEY IDEA:

Secondary axis allows:
✔ compare different scales
✔ sales vs cost vs profit
✔ financial dashboards

Very important in real analytics
"""