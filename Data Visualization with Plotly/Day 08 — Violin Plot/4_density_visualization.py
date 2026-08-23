# ======================================
# DENSITY VISUALIZATION
# ======================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("student_performance.csv")

# --------------------------------------
# Density-focused violin plot
# --------------------------------------

fig = px.violin(
    df,
    x="department",
    y="score",
    color="department",
    box=True,
    title="Density Visualization using Violin Plot"
)

# Improve layout
fig.update_layout(
    template="plotly_dark"
)

fig.show()

"""
KEY IDEA:

Violin plot is excellent for:
✔ statistical analysis
✔ distribution comparison
✔ density understanding

Compared to box plot:
- box plot summarizes
- violin plot shows shape
"""