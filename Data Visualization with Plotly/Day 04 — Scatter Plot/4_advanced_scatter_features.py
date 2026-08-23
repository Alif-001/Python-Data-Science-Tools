# ======================================
# ADVANCED SCATTER FEATURES
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("students.csv")

# --------------------------------------
# Advanced scatter plot
# --------------------------------------

fig = px.scatter(
    df,
    x="study_hours",
    y="marks",
    color="passed",
    symbol="gender",     # different shapes
    size="attendance",
    hover_data=["attendance", "gender", "passed"],
    title="Advanced Scatter Plot (Full Features)"
)

# --------------------------------------
# Hover customization (important!)
# --------------------------------------
fig.update_traces(
    marker=dict(opacity=0.8)
)

fig.update_layout(
    hovermode="closest"
)

fig.show()

"""
KEY FEATURES:

color   → category separation
size    → magnitude representation
symbol  → different shapes
hover_data → extra info on hover

This is REAL data science visualization style.
"""