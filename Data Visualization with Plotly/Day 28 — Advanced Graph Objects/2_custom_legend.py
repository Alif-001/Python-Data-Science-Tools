# ======================================
# CUSTOM LEGEND STYLING
# ======================================

import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("sales_finance.csv")

fig = go.Figure()

# Sales trace
fig.add_trace(go.Scatter(
    x=df["month"],
    y=df["sales"],
    name="Sales",
    line=dict(color="blue", width=3)
))

# Profit trace
fig.add_trace(go.Scatter(
    x=df["month"],
    y=df["profit"],
    name="Profit",
    line=dict(color="green", width=3, dash="dash")
))

# Marketing cost trace
fig.add_trace(go.Scatter(
    x=df["month"],
    y=df["marketing_cost"],
    name="Marketing Cost",
    line=dict(color="red", width=3, dash="dot")
))

# --------------------------------------
# Legend customization
# --------------------------------------

fig.update_layout(
    title="Custom Legend Styling",
    legend=dict(
        title="Business Metrics",
        bgcolor="lightgray",
        bordercolor="black",
        borderwidth=1
    )
)

fig.show()

"""
KEY IDEA:

Legend controls:
✔ labels
✔ colors
✔ line styles
✔ visual clarity
"""