# ======================================
# QUARTILES EXPLAINED
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("exam_scores.csv")

# --------------------------------------
# Box plot with points
# --------------------------------------

fig = px.box(
    df,
    y="score",
    points="all",   # show all data points
    title="Quartiles Visualization"
)

fig.show()

"""
IMPORTANT CONCEPTS:

Q1 = 25% of data below this
Q2 = Median (50%)
Q3 = 75% of data below this

Inside the box:
- middle line = median
- box edges = quartiles

This helps understand:
✔ data spread
✔ central tendency
"""