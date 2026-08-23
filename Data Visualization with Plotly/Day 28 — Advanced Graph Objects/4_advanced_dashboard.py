# ======================================
# ADVANCED BUSINESS DASHBOARD
# ======================================

import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("sales_finance.csv")

fig = go.Figure()

# Sales
fig.add_trace(go.Scatter(
    x=df["month"],
    y=df["sales"],
    name="Sales",
    line=dict(width=3)
))

# Profit
fig.add_trace(go.Scatter(
    x=df["month"],
    y=df["profit"],
    name="Profit",
    line=dict(width=3)
))

# Marketing cost
fig.add_trace(go.Scatter(
    x=df["month"],
    y=df["marketing_cost"],
    name="Marketing Cost",
    line=dict(width=3)
))

# --------------------------------------
# Advanced layout styling
# --------------------------------------

fig.update_layout(
    title="Advanced Business Dashboard",

    # background styling
    plot_bgcolor="white",
    paper_bgcolor="lightgray",

    # axis styling
    xaxis=dict(
        showgrid=False,
        title="Month"
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor="lightgray",
        title="Value"
    ),

    # legend position
    legend=dict(
        orientation="h",
        x=0.2,
        y=1.1
    ),

    font=dict(
        family="Arial",
        size=14
    )
)

fig.show()

"""
KEY IDEA:

Advanced dashboards include:
✔ clean UI
✔ readable legend
✔ structured layout
✔ professional design

This is production-level visualization
"""