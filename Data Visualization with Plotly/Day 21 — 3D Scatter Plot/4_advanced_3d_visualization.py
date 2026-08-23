# ======================================
# ADVANCED 3D VISUALIZATION
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("student_performance.csv")

# --------------------------------------
# Advanced 3D scatter visualization
# --------------------------------------

fig = px.scatter_3d(
    df,
    x="study_hours",
    y="sleep_hours",
    z="marks",
    color="attendance",
    size="attendance",
    hover_name="student",
    color_continuous_scale="Viridis",
    title="Advanced 3D Analytics Visualization"
)

# Improve axis titles
fig.update_layout(
    scene=dict(
        xaxis_title="Study Hours",
        yaxis_title="Sleep Hours",
        zaxis_title="Marks"
    )
)

fig.show()

"""
KEY IDEA:

This combines:
✔ 3D positioning
✔ color mapping
✔ size scaling
✔ interactive exploration

Used in advanced analytics dashboards
"""