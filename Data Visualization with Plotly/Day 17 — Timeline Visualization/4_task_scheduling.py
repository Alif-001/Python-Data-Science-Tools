# ======================================
# TASK SCHEDULING VISUALIZATION
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("project_tasks.csv")

df["start"] = pd.to_datetime(df["start"])
df["end"] = pd.to_datetime(df["end"])

# --------------------------------------
# Sort tasks by start date (IMPORTANT)
# --------------------------------------

df = df.sort_values("start")

# --------------------------------------
# Clean scheduling view
# --------------------------------------

fig = px.timeline(
    df,
    x_start="start",
    x_end="end",
    y="task",
    color="team",
    title="Task Scheduling Overview"
)

# Improve readability
fig.update_yaxes(autorange="reversed")

fig.show()

"""
KEY IDEA:

Scheduling helps:
✔ plan project workflow
✔ avoid task overlap conflicts
✔ improve productivity

Reversing y-axis gives classic Gantt view
"""