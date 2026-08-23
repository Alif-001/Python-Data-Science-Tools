# ======================================
# DAY 27: BASIC go.Figure()
# ======================================

import pandas as pd
import plotly.graph_objects as go

# Load dataset
df = pd.read_csv("sales_data.csv")

# --------------------------------------
# Create empty figure (Graph Objects style)
# --------------------------------------

fig = go.Figure()

# --------------------------------------
# Add line chart manually
# --------------------------------------

fig.add_trace(
    go.Scatter(
        x=df["month"],
        y=df["sales"],
        mode="lines+markers",  # line + points
        name="Sales"
    )
)

# --------------------------------------
# Layout customization
# --------------------------------------

fig.update_layout(
    title="Basic Graph Objects Example",
    xaxis_title="Month",
    yaxis_title="Sales"
)

fig.show()

"""
KEY IDEA:

Graph Objects:
✔ full manual control
✔ add_trace() builds chart step-by-step
✔ more flexible than Plotly Express
"""