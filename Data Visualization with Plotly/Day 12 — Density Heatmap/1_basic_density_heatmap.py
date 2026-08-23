# ======================================
# DAY 12: BASIC DENSITY HEATMAP
# ======================================

import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("student_data.csv")

# --------------------------------------
# Density Heatmap
# --------------------------------------

fig = px.density_heatmap(
    df,
    x="study_hours",
    y="marks",
    title="Study Hours vs Marks Density Heatmap"
)

fig.show()

"""
KEY IDEA:

Density heatmap shows:
✔ where data points are concentrated
✔ clusters of values
✔ patterns in 2D space

Darker / brighter areas = more data points
"""