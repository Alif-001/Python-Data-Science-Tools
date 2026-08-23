# ======================================
# DAY 26: BASIC SUBPLOTS
# ======================================

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load data
df = pd.read_csv("sales_data.csv")

# --------------------------------------
# Create subplot layout (2 rows, 1 column)
# --------------------------------------

fig = make_subplots(rows=2, cols=1)

# --------------------------------------
# First chart: Sales
# --------------------------------------

fig.add_trace(
    go.Scatter(x=df["month"], y=df["sales"], name="Sales"),
    row=1, col=1
)

# --------------------------------------
# Second chart: Profit
# --------------------------------------

fig.add_trace(
    go.Scatter(x=df["month"], y=df["profit"], name="Profit"),
    row=2, col=1
)

fig.update_layout(title="Basic Subplots Example")

fig.show()

"""
KEY IDEA:

Subplots allow:
✔ multiple charts in one figure
✔ better comparison
✔ dashboard-style layout
"""