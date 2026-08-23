# ======================================
# PROCESS ANALYSIS FUNNEL
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("funnel_data.csv")

# --------------------------------------
# Process-focused funnel chart
# --------------------------------------

fig = px.funnel(
    df,
    x="value",
    y="stage",
    title="Process Flow Analysis (User Journey)"
)

# Improve layout
fig.update_layout(
    yaxis_title="Stages of Process"
)

fig.show()

"""
KEY IDEA:

Funnel charts are used for:
✔ process optimization
✔ user journey tracking
✔ identifying bottlenecks
"""