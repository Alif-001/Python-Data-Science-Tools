# ======================================
# DAY 2: PLOTLY EXPRESS INTRO
# ======================================

import pandas as pd
import plotly.express as px

# --------------------------------------
# Load dataset
# --------------------------------------
df = pd.read_csv("sales.csv")

print(df)

# --------------------------------------
# Plotly Express (px)
# --------------------------------------
"""
Plotly Express is:
- The easiest way to create charts
- High-level API
- Less code, fast results
"""

# Simple line chart
fig = px.line(
    df,
    x="day",
    y="sales",
    title="Sales Trend (Plotly Express)"
)

fig.show()

# --------------------------------------
# Key idea:
# px automatically builds the figure for you
# --------------------------------------