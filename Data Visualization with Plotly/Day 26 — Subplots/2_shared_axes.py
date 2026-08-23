# ======================================
# SUBPLOTS WITH SHARED AXES
# ======================================

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("sales_data.csv")

# --------------------------------------
# Shared x-axis (month)
# --------------------------------------

fig = make_subplots(
    rows=2,
    cols=1,
    shared_xaxes=True   # important concept
)

# Sales chart
fig.add_trace(
    go.Scatter(x=df["month"], y=df["sales"], name="Sales"),
    row=1, col=1
)

# Profit chart
fig.add_trace(
    go.Scatter(x=df["month"], y=df["profit"], name="Profit"),
    row=2, col=1
)

fig.update_layout(title="Shared X-Axis Subplots")

fig.show()

"""
KEY IDEA:

shared_xaxes=True means:
✔ both charts use same timeline
✔ better comparison
✔ aligned visualization
"""