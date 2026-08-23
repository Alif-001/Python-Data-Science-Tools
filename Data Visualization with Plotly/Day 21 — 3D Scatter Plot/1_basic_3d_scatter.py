# ======================================
# DAY 21: BASIC 3D SCATTER PLOT
# ======================================

import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("student_performance.csv")

# --------------------------------------
# Basic 3D scatter plot
# --------------------------------------

fig = px.scatter_3d(
    df,
    x="study_hours",
    y="sleep_hours",
    z="marks",
    title="3D Student Performance Visualization"
)

fig.show()

"""
KEY IDEA:

3D scatter plot shows:
✔ relationship among 3 variables
✔ spatial visualization
✔ deeper pattern analysis

Axes:
X = study_hours
Y = sleep_hours
Z = marks
"""