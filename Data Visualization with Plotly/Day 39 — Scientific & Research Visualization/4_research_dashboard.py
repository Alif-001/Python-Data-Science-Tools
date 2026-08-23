# ======================================
# DAY 39: RESEARCH DASHBOARD (MULTI-VIEW)
# ======================================

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("experiment_data.csv")

# --------------------------------------
# Create multi-plot research dashboard
# --------------------------------------

fig = make_subplots(
    rows=1,
    cols=2,
    subplot_titles=("Temperature Trend", "Pressure Trend")
)

# Temperature plot
fig.add_trace(
    go.Scatter(
        x=df["time"],
        y=df["temperature"],
        mode="lines+markers",
        name="Temperature"
    ),
    row=1, col=1
)

# Pressure plot
fig.add_trace(
    go.Scatter(
        x=df["time"],
        y=df["pressure"],
        mode="lines+markers",
        name="Pressure"
    ),
    row=1, col=2
)

fig.update_layout(
    title="Research Dashboard: Experiment Analysis",
    showlegend=False
)

fig.show()

"""
KEY IDEA:

✔ research paper style visualization
✔ multiple experiment variables
"""