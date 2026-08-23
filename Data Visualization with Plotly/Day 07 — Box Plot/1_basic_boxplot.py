# ======================================
# DAY 7: BASIC BOX PLOT
# ======================================

import pandas as pd
import plotly.express as px

# --------------------------------------
# Load dataset
# --------------------------------------
df = pd.read_csv("exam_scores.csv")

print(df)

# --------------------------------------
# Basic box plot
# --------------------------------------

fig = px.box(
    df,
    y="score",
    title="Distribution of Exam Scores"
)

fig.show()

"""
KEY IDEA:

Box plot helps visualize:
✔ distribution
✔ median
✔ spread
✔ outliers

Very useful in statistics.
"""