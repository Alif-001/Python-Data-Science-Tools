# ======================================
# GRAPH OBJECTS BAR CHART
# ======================================

import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("sales_data.csv")

# --------------------------------------
# Create figure
# --------------------------------------

fig = go.Figure()

# --------------------------------------
# Add bar chart
# --------------------------------------

fig.add_trace(
    go.Bar(
        x=df["month"],
        y=df["sales"],
        name="Monthly Sales",
        marker_color="blue"
    )
)

fig.add_trace(
    go.Bar(
        x=df["month"],
        y=df["profit"],
        name="Profit",
        marker_color="green"
    )
)

# --------------------------------------
# Layout settings
# --------------------------------------

fig.update_layout(
    title="Sales vs Profit (Bar Chart)",
    barmode="group"  # side-by-side bars
)

fig.show()

"""
KEY IDEA:

barmode options:
✔ group → side-by-side
✔ stack → stacked bars

Graph Objects = full control
"""