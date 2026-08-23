# ======================================
# FIGURE OBJECT BASICS
# ======================================

import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("sales.csv")

# --------------------------------------
# Graph Objects (go)
# --------------------------------------
"""
Graph Objects = Low-level control

You build chart step-by-step:
- Figure
- Traces
- Layout
"""

# Create empty figure
fig = go.Figure()

# Add a line trace manually
fig.add_trace(
    go.Scatter(
        x=df["day"],
        y=df["sales"],
        mode="lines+markers",
        name="Sales"
    )
)

# Show result
fig.show()

"""
WHY USE THIS?

✔ Full control
✔ Multiple charts in one figure
✔ Advanced customization
"""