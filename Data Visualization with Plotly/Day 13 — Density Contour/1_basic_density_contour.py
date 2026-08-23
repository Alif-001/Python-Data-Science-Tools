# ======================================
# DAY 13: BASIC DENSITY CONTOUR
# ======================================

import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("student_data.csv")

# --------------------------------------
# Basic density contour plot
# --------------------------------------

fig = px.density_contour(
    df,
    x="study_hours",
    y="marks",
    title="Study Hours vs Marks - Density Contour"
)

fig.show()

"""
KEY IDEA:

Contour plot shows:
✔ density regions
✔ smooth distribution
✔ data concentration areas

Instead of points, we see "levels"
"""