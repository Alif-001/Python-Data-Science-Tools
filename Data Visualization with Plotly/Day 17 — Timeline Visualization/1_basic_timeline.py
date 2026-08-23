# ======================================
# DAY 17: BASIC TIMELINE VISUALIZATION
# ======================================

import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("project_tasks.csv")

# Convert to datetime (IMPORTANT for timeline)
df["start"] = pd.to_datetime(df["start"])
df["end"] = pd.to_datetime(df["end"])

# --------------------------------------
# Basic timeline chart
# --------------------------------------

fig = px.timeline(
    df,
    x_start="start",
    x_end="end",
    y="task",
    title="Project Timeline Overview"
)

fig.show()

"""
KEY IDEA:

Timeline chart shows:
✔ when each task starts and ends
✔ project schedule visually
✔ overlapping tasks

Very useful in project management
"""