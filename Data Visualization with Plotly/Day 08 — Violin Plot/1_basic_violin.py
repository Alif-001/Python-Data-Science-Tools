# ======================================
# DAY 8: BASIC VIOLIN PLOT
# ======================================

import pandas as pd
import plotly.express as px

# --------------------------------------
# Load dataset
# --------------------------------------
df = pd.read_csv("student_performance.csv")

print(df)

# --------------------------------------
# Basic violin plot
# --------------------------------------

fig = px.violin(
    df,
    y="score",
    title="Distribution of Student Scores"
)

fig.show()

"""
KEY IDEA:

Violin plot shows:
✔ distribution shape
✔ spread of data
✔ density of values

It is more informative than a box plot.
"""