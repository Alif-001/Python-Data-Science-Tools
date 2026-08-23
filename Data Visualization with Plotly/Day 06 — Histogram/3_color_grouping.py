# ======================================
# COLOR GROUPING
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("student_scores.csv")

# --------------------------------------
# Histogram with color grouping
# --------------------------------------

fig = px.histogram(
    df,
    x="math_score",
    color="gender",
    barmode="overlay",
    title="Math Score Distribution by Gender"
)

# Make bars slightly transparent
fig.update_traces(opacity=0.7)

fig.show()

"""
KEY IDEA:

color=
→ separates categories

barmode="overlay"
→ bars overlap

Useful for:
✔ comparing distributions
✔ group analysis
"""