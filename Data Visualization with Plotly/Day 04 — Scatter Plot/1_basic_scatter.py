# ======================================
# DAY 4: BASIC SCATTER PLOT
# ======================================

import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("students.csv")

# --------------------------------------
# Basic scatter plot
# --------------------------------------

fig = px.scatter(
    df,
    x="study_hours",
    y="marks",
    title="Study Hours vs Marks"
)

fig.show()

"""
KEY IDEA:

Scatter plot shows:
✔ relationship between two variables
✔ pattern (positive/negative correlation)
✔ outliers
"""