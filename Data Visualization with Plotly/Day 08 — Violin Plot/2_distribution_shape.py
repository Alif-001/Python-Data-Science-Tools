# ======================================
# DISTRIBUTION SHAPE
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("student_performance.csv")

# --------------------------------------
# Violin plot with box and points
# --------------------------------------

fig = px.violin(
    df,
    y="score",
    box=True,        # adds box plot inside
    points="all",    # show all points
    title="Distribution Shape Visualization"
)

fig.show()

"""
KEY IDEA:

Wider area in violin =
more data concentrated there

Narrow area =
fewer data points

This helps visualize:
✔ density
✔ distribution shape
✔ concentration of scores
"""