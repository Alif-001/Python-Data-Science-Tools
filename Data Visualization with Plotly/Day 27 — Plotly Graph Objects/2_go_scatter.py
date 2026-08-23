# ======================================
# GRAPH OBJECTS SCATTER PLOT
# ======================================

import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("sales_data.csv")

# --------------------------------------
# Create figure
# --------------------------------------

fig = go.Figure()

# --------------------------------------
# Scatter plot (manual control)
# --------------------------------------

fig.add_trace(
    go.Scatter(
        x=df["sales"],
        y=df["profit"],
        mode="markers",   # only points
        marker=dict(
            size=10,
            color=df["profit"],  # color by profit
            colorscale="Viridis",
            showscale=True
        ),
        name="Sales vs Profit"
    )
)

fig.update_layout(
    title="Graph Objects Scatter Plot",
    xaxis_title="Sales",
    yaxis_title="Profit"
)

fig.show()

"""
KEY IDEA:

You control:
✔ marker size
✔ color scale
✔ axis labels
✔ everything manually
"""