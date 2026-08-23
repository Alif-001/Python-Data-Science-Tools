# ======================================
# GANTT CHART (CLASSIC PROJECT VIEW)
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("project_tasks.csv")

df["start"] = pd.to_datetime(df["start"])
df["end"] = pd.to_datetime(df["end"])

# --------------------------------------
# Gantt-style timeline (same as timeline but styled)
# --------------------------------------

fig = px.timeline(
    df,
    x_start="start",
    x_end="end",
    y="task",
    color="team",   # grouping by team
    title="Gantt Chart - Project Breakdown"
)

fig.show()

"""
KEY IDEA:

Gantt chart helps:
✔ visualize project structure
✔ assign team responsibilities
✔ track progress per department
"""