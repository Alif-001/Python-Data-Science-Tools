# ======================================
# PROJECT TRACKING TIMELINE
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("project_tasks.csv")

df["start"] = pd.to_datetime(df["start"])
df["end"] = pd.to_datetime(df["end"])

# --------------------------------------
# Add duration column (very useful)
# --------------------------------------

df["duration_days"] = (df["end"] - df["start"]).dt.days

print(df)

# --------------------------------------
# Timeline with color by duration
# --------------------------------------

fig = px.timeline(
    df,
    x_start="start",
    x_end="end",
    y="task",
    color="duration_days",
    title="Project Tracking (Duration View)"
)

fig.show()

"""
KEY IDEA:

Duration helps answer:
✔ which task takes longest
✔ bottlenecks in project
✔ workload distribution
"""